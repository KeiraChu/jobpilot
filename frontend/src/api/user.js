import { request } from '../utils/request'

// 用户登录
export function userLogin(params) {
    return request({
        method: 'post',
        url: `/login`,
        data: params,
        headers: {
            'Authorization': window.localStorage.token,
        },
    })
}

// 用户注册
export function userRegister(params) {
    return request({
        method: 'post',
        url: `/register/submit`,
        data: params,
        headers: {
            'Authorization': window.localStorage.token,
        },
    })
}
// 检查验证码
export function getCaptcha(params) {
    return request({
        method: 'get',
        url: `/register/captcha`,
        params,
        headers: {
            'Authorization': window.localStorage.token,
        },
    })
}
// 检查验证码
export function verifyCaptcha(params) {
    return request({
        method: 'post',
        url: `/register/verify`,
        data: params,
        headers: {
            'Authorization': window.localStorage.token,
        },
    })
}
