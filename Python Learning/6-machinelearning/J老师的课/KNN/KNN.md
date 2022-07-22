#### 交叉验证

- 训练集
- 验证集
- 测试集

#### 特征缩放：

- 线性归一化：

  $$
  Xnew = \frac{X-Xmin}{Xmax-Xmin}
  $$

  $$
  Xnew\in[0,1]
  $$
- 标准差标准化：推荐

  $$
  Xnew=\frac{X-Xmean}{Xstd}
  $$

  $$
  Xmean = \frac{X1+X2+X3+...+Xn}{n}
  $$

  $$
  Xstd = \sqrt{\frac{(X1-Xmean)^2+(X2-Xmean)^2+...(Xn-Xmean)^2}{n}}
  $$

#### 特征编码

- Label Encoding ==> One-Hot Encoding
