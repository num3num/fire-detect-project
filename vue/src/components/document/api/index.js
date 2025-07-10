import request from '../../../utils/request'

export const docUpload = (file) => {
    return request({
        method:'post',
        url:`/v1/detect?file_path=${file.file_path}&sava_path=${file.sava_path}`
    } )
}