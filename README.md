# 使用步骤
* version:20220913
1. 双击bin2c.exe

2. 输入图片所在文件夹，如：D:\images，请确保images文件夹下都是需要转换的图片文件

3. 输入目标c文件存放的文件夹，如：D:\c_files

4. 回车即可生成

备注：
1. 如果图片名称带有空格或"-"，在转成结构体时由于结构体名称不能有空格和"-"，所以会自动转成"_"

2. 如果图片名称有中文或其它特殊字符，程序会停止

3. sd_res_template.c存放了模板文件，bin2c.exe会读取模板文件并替换模板文件中有{XXX}的部分，如果需要添加新的内容，你可以随时更改模板。  
模板文件中替换内容解释：  
* {NAME_LOWER}: 图片文件名（不带后缀）  
* {NAME_UPPER}: 图片文件名转大写（不带后缀）  
* {BIN_RAW}: 二进制图片数据  
* {DATA_RAW}: 本来想写成解码后的图片数据，但是这个功能暂时不需要，所以现在和{BIN_RAW}一样  
* {DATA_SIZE}: 图片（c结构体内数据）的大小  



