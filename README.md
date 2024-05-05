# Pythonで遊ぼう

## ディレクトリ構造

```bash
% tree .
.
├── README.md
├── pyproject.toml # Pythonプロジェクトの設定ファイル（pytest, mypy: 静的型付けリンター）
├── tox.ini # toxの設定ファイル（tox: 継続的インテグレーション）
├── requirements.txt # pipでインストールできるPythonのパッケージ
├── src # 課題用ソースコードの一覧。関数を課題に沿った内容に修正して使ってください
│   ├── challenge_001.py
│   └── challenge_002.py
└── tests # 課題用テストコードの一覧。足りてない観点があれば教えてください
    ├── test_challenge_001.py
    └── test_challenge_002.py
```

## 環境構築の手順

仮想環境を作成します。

```bash
python3 -m venv venv
```

作成した仮想環境を有効化します。

```bash
source venv/bin/activate
```

仮想環境に必要なパッケージをインストールします。

```bash
pip install -r requirements.txt
```

仮想環境から抜ける場合は、次のコマンドを実行します。

```bash
deactivate
```

再び仮想環境に入りたい場合は、仮想環境を有効化するコマンドを実行します。

```bash
source venv/bin/activate
```

## 使い方

プロジェクトのルートディレクトリで、pytestを実行してください。

全てのテストファイルを実行したい場合。

```bash
pytest
```

特定のテストファイルを実行したい場合。

```bash
pytest tests/test_challenge_001.py
```

特定のテスト関数だけ実行したい場合。

```bash
pytest tests/test_challenge_001.py::test_to_fahrenheit
```

テストの詳細を確認したい場合、 `-vv`オプションを設定します。

```bash
pytest -vv tests/test_challenge_001.py::test_to_fahrenheit
```
