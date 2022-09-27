# https://docs.streamlit.io/library/api-reference

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f'Interation {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせを書く')


# st.sidebarでサイドバーに
input_text = st.text_input('あなたの趣味を教えてください')
# option =  st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1, 11))
# )

# condition = st.slider('あなたの今の調子は?', 0, 100, 50)
# 'コンディション:', condition

# 'あなたの趣味:', input_text
# 'コンディション', condition

#チェックボックスで表示
# if st.checkbox('Show Image'):
#     img = Image.open('7.jpg')
#     st.image(img, caption='7.jpg',use_column_width=True)

#経度、緯度の座標
# df = pd.DataFrame(
#     np.random.rand(100, 2)/[ 50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )

# st.map(df)

# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)


#write, dataframeでも良い、tableは静的
#st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

