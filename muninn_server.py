import sys,datetime
import convert
import fatch_data
temperr, tempout = sys.stderr, sys.stdout
sys.stderr = sys.stdout = open("muninn_server.log","a+")
print("="*30,"脚本正在运行...%s"%str(datetime.datetime.today()))
print("正在迁移 Jupyter Notebook 文件夹，并进行文件转换")
convert.get_file()
print("正在构建HTML文档...")
fatch_data.main(update_data=True,file_path="last.data")
print("正在上传至Github服务器")
convert.submit()