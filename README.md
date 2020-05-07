# Nuclear Experiment Yamero
直近の地震を近くの大学に因縁づけるタグをツイートします。名前は適当に付けました。

### Description
実行すると、いろいろな API を使って地震情報や周辺の大学名を取得してタグを生成し、自動でツイートを行います。
利用した外部サービスは以下の通りです:
- [P2P地震情報 JSON API]{https://www.p2pquake.net/dev/json-api/}
- [Place Search]{https://developers.google.com/places/web-service/search}
- [Twitter Developers]{https://developer.twitter.com/}

### Usage
1. .env に必要な API キーを書いておく
2. 上の .env と同じディレクトリに NuclearExperimentYamero.py を置く
3. NuclearExperimentYamero.py を実行する
4. コンソールにツイートされるタグが表示されるので、確認後ツイートして良ければ 'y' を入力するとタグがツイートされます。
5. 'y' 以外が入力されると、ツイートせずに終了します。空行のまま Enter を押した場合もツイートはキャンセルされます。

### Note
バグ報告やアドバイス(「こんな機能つけてみたら？」「これもっと簡単に出来るよ」)等あればぜひお願いします。
