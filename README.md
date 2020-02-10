# 手書き数字判定アプリケーション
![mnist_s3_before](https://user-images.githubusercontent.com/55865542/66296926-94bf3280-e929-11e9-97c5-6fc407f046ee.png)
</br>
![mnist_s3_after](https://user-images.githubusercontent.com/55865542/66296947-9db00400-e929-11e9-851c-aad6acffc40a.png)

# AWS上で動作
本アプリケーションは、AWS上で動作することを想定しています。
## contents
judge.htmlおよびsvc.joblibをS3に配置し、HTMLファイルを静的コンテンツとして配信してください。

## lambda_function
main.pyをaws lambdaの関数として登録してください。
以下の３つのライブラリのソースコードをmain.pyと同じ階層に配置してください。
```lambda_function
main.py
/sklearn
/PIL
/joblib
```

