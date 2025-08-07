from fastapi import APIRouter, File, UploadFile, HTTPException
from typing import List
import os
import aiofiles

app05 = APIRouter()


@app05.post("/file")
async def get_file(file: bytes = File()):
    # 适合小文件上传 因为会直接把数据跑到用户内存
    print("file", file)  # 后面的file接受的是你上传文件的字节流
    return {
        # 这里注意只能存在一个
        # "file": "file"
        "file": len(file)
    }


@app05.post("/files")
async def get_files(files: List[bytes] = File()):  # 列表里面放多个文件按

    for file in files:
        print(len(file))

    return {
        "file": len(files)
    }


@app05.post("/uploadFile")
async def get_upload_file(file: UploadFile):  # 列表里面放多个文件按
    print("file", file)

    path = os.path.join("images", file.filename)

    with open(path,"wb") as f:
        for line in file.file:
            f.write(line)

    return {
        "file": file.filename
    }


# 确保保存目录存在（如不存在则创建）
SAVE_DIR = "images"
os.makedirs(SAVE_DIR, exist_ok=True)  # exist_ok=True 避免目录已存在时报错

@app05.post("/uploadFiles")
async def get_upload_files(files: List[UploadFile]):  # 列表里面放多个文件按
    print("file", files)

    return{
        "names": [file.filename for file in files]
    }

# 下面上传多个文件并保存到images
# async def upload_and_save_files(
#         files: List[UploadFile] = File(...)  # 显式标记文件参数
# ):
#     saved_files = []
#
#     for file in files:
#         try:
#             # 构建完整保存路径（防止文件名重复）
#             filename = file.filename
#             save_path = os.path.join(SAVE_DIR, filename)
#
#             # 处理文件名重复的情况（如果文件已存在，添加序号）
#             counter = 1
#             while os.path.exists(save_path):
#                 name, ext = os.path.splitext(filename)
#                 save_path = os.path.join(SAVE_DIR, f"{name}_{counter}{ext}")
#                 counter += 1
#
#             # 异步保存文件（推荐使用aiofiles，避免阻塞事件循环）
#             async with aiofiles.open(save_path, "wb") as f:
#                 content = await file.read()  # 一次性读取文件内容
#                 await f.write(content)
#
#             saved_files.append({
#                 "original_name": filename,
#                 "saved_path": save_path,
#                 "content_type": file.content_type,
#                 "size": len(content)  # 文件大小（字节）
#             })
#
#         except Exception as e:
#             # 捕获单个文件保存失败的错误，不影响其他文件
#             raise HTTPException(
#                 status_code=500,
#                 detail=f"保存文件 {file.filename} 失败: {str(e)}"
#             )
#
#     return {
#         "message": f"成功保存 {len(saved_files)} 个文件",
#         "files": saved_files
#     }