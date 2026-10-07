import { request } from '../utils/request'

export function selectPosition(params) {
    return request({
        method: 'post',
        url: `/resume/submit`,
        data: params,
        headers: {
            'Authorization': `Bearer ${window.localStorage.token || ''}`,
        },
    })
}

export function uploadResume(file, targetRole) {
    const data = new FormData()
    data.append('file', file)
    data.append('targetRole', targetRole || '')
    return request({ method: 'post', url: '/upload', data })
}

export function createCareerPlan(profile, match) {
    return request({ method: 'post', url: '/ai/career-plan', data: { profile, match } })
}

export function recommendWithProfile(profile) {
    return request({ method: 'post', url: '/ai/recommend', data: { profile } })
}

export function submitRecommendationFeedback(positionId, action) {
    return request({ method: 'post', url: `/positions/${positionId}/feedback`, data: { action } })
}
