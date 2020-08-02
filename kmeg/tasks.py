
from kmeg.quantisation import to_reconst_kmeg
import os


def perform_quantization_task(task_details):
    print("received the payload:",task_details)
    original_img_path = task_details.get("jpeg_picture_path")
    clusters = task_details.get("clusters")
    original_img_filenm, ext = os.path.splitext(original_img_path)
    original_img_reconst_path = original_img_filenm + "_reconst" + ext

    to_reconst_kmeg(original_img_path, clusters, original_img_reconst_path)
    tb_nail_img_path = original_img_filenm + "_tb" + ext
    tb_nail_img_filenm, ext = os.path.splitext(tb_nail_img_path)
    tb_nail_reconst_path = tb_nail_img_filenm + "_reconst" + ext
    to_reconst_kmeg(tb_nail_img_path, clusters, tb_nail_reconst_path)
    print("completed quantization for id=", task_details.get("id"))