<template>
  <main class="copilot">
    <section class="hero">
      <div>
        <p class="eyebrow">JOBPILOT AI COPILOT</p>
        <h1>让每一次职位推荐都有证据</h1>
        <p>上传真实简历，获得结构化能力画像、人岗匹配拆解、技能差距和 60 天求职准备计划。</p>
      </div>
      <div class="upload-card">
        <el-input v-model="targetRole" placeholder="目标岗位，例如：AI 应用开发实习生" />
        <input ref="file" type="file" accept=".pdf,.docx,.txt,.md" @change="selectFile">
        <el-button type="primary" :loading="loading" @click="analyze">开始分析</el-button>
        <small>支持 PDF、DOCX、TXT、Markdown，最大 20MB</small>
      </div>
    </section>

    <el-alert v-for="warning in warnings" :key="warning" :title="warning" type="warning" show-icon />

    <section v-if="profile" class="panel">
      <header><h2>简历能力画像</h2><span>解析置信度 {{ Math.round(profile.confidence * 100) }}%</span></header>
      <p class="hint">AI 解析结果需要你确认。删除误识别技能，或补充简历中确实存在的技能后重新匹配。</p>
      <div class="skills">
        <el-tag v-for="skill in profile.skills" :key="skill" closable @close="removeSkill(skill)">{{ skill }}</el-tag>
        <el-input v-if="skillInputVisible" ref="skillInput" v-model="skillInput" size="small" class="skill-input" @keyup.enter.native="addSkill" @blur="addSkill" />
        <el-button v-else size="small" @click="showSkillInput">+ 添加真实技能</el-button>
      </div>
      <p v-if="!profile.skills.length">尚未识别到标准化技能，请完善简历中的技术栈和项目描述。</p>
      <el-button type="primary" :loading="reranking" class="rerank" @click="rerank">确认画像并重新匹配</el-button>
    </section>

    <section v-if="matches.length" class="results">
      <article v-for="match in matches" :key="match.position.position_id" class="match-card">
        <div class="score">{{ Math.round(match.score) }}<small>匹配分</small></div>
        <div class="match-main">
          <header>
            <div><h2>{{ match.position.title }}</h2><p>{{ match.position.company }} · {{ match.position.address }} · {{ match.position.salary }}</p></div>
            <el-button @click="makePlan(match)">生成准备计划</el-button>
          </header>
          <div class="breakdown">
            <span>语义 {{ match.breakdown.semantic }}%</span>
            <span>技能 {{ match.breakdown.skill_coverage }}%</span>
            <span>方向 {{ match.breakdown.preference }}%</span>
            <span>硬条件 {{ match.breakdown.hard_constraints }}%</span>
          </div>
          <div class="columns">
            <div><h3>匹配证据</h3><p v-for="item in match.reasons" :key="item">✓ {{ item }}</p></div>
            <div><h3>需要补足</h3><p v-for="item in match.risks" :key="item">△ {{ item }}</p></div>
          </div>
          <div class="feedback">
            <span>这个推荐有帮助吗？</span>
            <el-button size="mini" @click="feedback(match, 'LIKE')">有帮助</el-button>
            <el-button size="mini" @click="feedback(match, 'DISLIKE')">不相关</el-button>
            <el-button size="mini" type="primary" plain @click="feedback(match, 'APPLIED')">已投递</el-button>
          </div>
        </div>
      </article>
    </section>

    <el-dialog title="60 天求职准备计划" :visible.sync="planVisible" width="720px">
      <div v-if="plan">
        <el-alert :title="plan.guardrail" type="info" show-icon />
        <h3>简历修改建议</h3><p v-for="item in plan.resume_suggestions" :key="item">• {{ item }}</p>
        <h3>面试准备</h3><p v-for="item in plan.interview_questions" :key="item">• {{ item }}</p>
        <h3>学习路线</h3>
        <div v-for="step in plan.learning_plan" :key="step.week" class="step">
          <strong>第 {{ step.week }} 周：{{ step.goal }}</strong><p>{{ step.actions.join('；') }}</p>
        </div>
      </div>
    </el-dialog>
  </main>
</template>

<script>
import { createCareerPlan, recommendWithProfile, submitRecommendationFeedback, uploadResume } from '../api/position'

export default {
  data: () => ({ targetRole: 'AI 应用开发实习生', file: null, loading: false, reranking: false, profile: null, matches: [], warnings: [], plan: null, planVisible: false, skillInputVisible: false, skillInput: '' }),
  methods: {
    selectFile(event) { this.file = event.target.files[0] },
    removeSkill(skill) { this.profile.skills = this.profile.skills.filter(item => item !== skill) },
    showSkillInput() { this.skillInputVisible = true; this.$nextTick(() => this.$refs.skillInput.focus()) },
    addSkill() {
      const value = this.skillInput.trim()
      if (value && !this.profile.skills.includes(value)) this.profile.skills.push(value)
      this.skillInput = ''
      this.skillInputVisible = false
    },
    async analyze() {
      if (!this.file) return this.$message.warning('请先选择简历文件')
      this.loading = true
      try {
        const response = await uploadResume(this.file, this.targetRole)
        if (response.code !== 200) throw new Error(response.msg)
        this.profile = response.data.profile
        this.matches = response.data.results || []
        this.warnings = response.data.warnings || []
      } catch (error) {
        this.$message.error(error.message || '分析失败')
      } finally { this.loading = false }
    },
    async rerank() {
      this.reranking = true
      try {
        const response = await recommendWithProfile(this.profile)
        if (response.code !== 200) throw new Error(response.msg)
        this.matches = response.data.results || []
        this.warnings = response.data.warnings || []
        this.$message.success('已按确认后的能力画像重新匹配')
      } catch (error) { this.$message.error(error.message || '重新匹配失败') }
      finally { this.reranking = false }
    },
    async feedback(match, action) {
      try {
        const response = await submitRecommendationFeedback(match.position.position_id, action)
        if (response.code !== 200) throw new Error(response.msg)
        this.$message.success('反馈已记录，将用于后续推荐评测')
      } catch (error) { this.$message.error(error.message || '反馈提交失败') }
    },
    async makePlan(match) {
      try {
        const response = await createCareerPlan(this.profile, match)
        if (response.code !== 200) throw new Error(response.msg)
        this.plan = response.data
        this.planVisible = true
      } catch (error) { this.$message.error(error.message || '计划生成失败') }
    }
  }
}
</script>

<style scoped>
.copilot{min-height:100vh;background:#f4f7fb;padding:40px 7%;color:#152238}.hero{display:grid;grid-template-columns:1.4fr 1fr;gap:30px;padding:42px;border-radius:24px;background:linear-gradient(135deg,#081d3a,#1454a3);color:white}.hero h1{font-size:40px;margin:8px 0 16px}.eyebrow{letter-spacing:2px;color:#7dd3fc}.upload-card{display:flex;flex-direction:column;gap:14px;background:white;color:#526174;padding:24px;border-radius:16px}.panel,.match-card{background:white;border-radius:18px;padding:24px;margin-top:22px;box-shadow:0 8px 30px rgba(15,42,80,.07)}.panel header,.match-main header{display:flex;justify-content:space-between;align-items:center}.hint{color:#667085}.skills{display:flex;gap:8px;flex-wrap:wrap}.skill-input{width:150px}.rerank{margin-top:18px}.match-card{display:flex;gap:24px}.score{width:90px;height:90px;border-radius:50%;background:#e7f1ff;color:#0759bd;display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:30px;font-weight:bold;flex:none}.score small{font-size:12px}.match-main{flex:1}.breakdown{display:flex;gap:12px;flex-wrap:wrap;margin:18px 0}.breakdown span{background:#f0f5fb;padding:7px 12px;border-radius:8px}.columns{display:grid;grid-template-columns:1fr 1fr;gap:24px}.feedback{display:flex;align-items:center;gap:8px;margin-top:18px;padding-top:14px;border-top:1px solid #edf1f6;color:#667085}.step{border-left:3px solid #1677ff;padding-left:14px;margin:14px 0}@media(max-width:800px){.hero,.columns{grid-template-columns:1fr}.match-card{flex-direction:column}.feedback{flex-wrap:wrap}}
</style>
