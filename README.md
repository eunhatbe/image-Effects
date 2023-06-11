## Image Effects


### Example
#### pencil drawing
<img src="https://github.com/eunhatbe/pencil-drawing/blob/main/img/city.png" width="400" height="400"/>
<img src="https://github.com/eunhatbe/pencil-drawing/blob/main/pencilcity.png" width="400" height="400"/>




### package
```text


```

### Error

이미지 처리중 특정 이미지는 해당 에러를 일으킴
```text
Process finished with exit code -1073741819 (0xC0000005)


solution:

from pympler import muppy
all_objects=muppy.get_objects()  # this causes pydev debugger exit with code -1073741819 (0xC0000005)
```