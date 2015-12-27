import subprocess

epoch_time_obj = subprocess.Popen(["date", "+%s"], stdout=subprocess.PIPE)
epoch_time = epoch_time_obj.communicate()[0]
file_name = epoch_time[:-1] + "-temp_name"
print file_name
