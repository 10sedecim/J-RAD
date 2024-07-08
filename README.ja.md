# Japanese Rhetoric Annotation Dataset (J-RAD)

This project is available in multiple languages:
- [English](README.md)
- [日本語](README.ja.md)

## 概要
**Japanese Rhetoric Annotation Dataset (J-RAD)** は、修辞法(rhetorical devices)アノテーションつき日本語テキストデータセットです。  
本データセットは、日本語の文体分析やスタイロメトリーにおいて修辞法の分析を行うために作成されました。  
J-RADは、LLM（大規模言語モデル）を用いて自動生成された、修辞法を含むテキストデータを提供します。

## 背景
日本語の文体分析やスタイロメトリーにおいて、修辞法の分析は重要ですが、修辞法を用いた十分なデータセットが存在しませんでした。  
また、実在の小説を用いた修辞法アノテーションには、ラベル不均衡や著作権による制限がありました。  
J-RADは、LLMを用いて修辞法を用いたテキストを自動生成することで、この課題を解決することを目指しています。

## データセットの構成
- `data/raw`
  - [`single_rhetorical_device`](./data/raw/single_rhetorical_device):  
   各修辞法ごとに、その修辞法のみを利用したテキストが格納されています。  
   修辞法ごとに個別のJSONファイルに分割され、それそれのファイルには500テキストが含まれています。
  - [`multiple_rhetorical_devices`](./data/raw/multiple_rhetorical_devices):  
  ランダムに複数の修辞法を利用したテキストが格納されています。  
  1000サンプルごとにJSONファイルに分割され、それぞれのファイルには1000テキストが含まれており、合計で100,000テキストが含まれます。

- metadata
  - [`scripts/rhetorical_devices.py`](./scripts/rhetorical_devices.py):  
  修辞法の種類および説明が格納されています。現在のバージョンでは、153種の修辞法を収録しています。
  - [`./metadata/rhetorical_device_counts.csv`](./metadata/rhetorical_device_counts.csv)  
  データセット全体の統計が格納されています。現在のバージョンでは、合計444,652個の修辞法を収録しています。

## サンプル
```json
[
    {
        "id": "epitrope_0",
        "rhetorical_device": [
            "epitrope"
        ],
        "text": "新しいカヤックの機能性については、私はこのように評価しているのですが、あなたはどのように感じられますか?私の意見に同意されますか?"
    },
    {
        "id": "isocolon_0",
        "rhetorical_device": [
            "isocolon"
        ],
        "text": "予防医療は健康を守り、医療費を抑える。定期検診を受け、生活習慣を改善することが大切だ。"
    },
    {
        "id": "metonymy_0",
        "rhetorical_device": [
            "metonymy"
        ],
        "text": "スピアフィッシングの聖地、沖縄の海で、熟練のダイバーたちが魚を狙っていた。"
    },
    ...
]
```
([全体を表示](./data/sample/samples.json))

## ライセンス
本データセットは、CC BY-NC-SA 4.0ライセンスのもとで公開されています。  
商業目的での使用はできません。非商業目的であれば、適切なクレジットを付与することで自由に利用できます。

## 先行研究
J-RADの先行研究として[J-FIG](https://www.kotorica.net/j-fig/info/guideline)があります。  
J-FIGは実在の日本語テキストに修辞法アノテーションを行ったデータセットであり、J-RADよりも自然な日本語のデータセットです。  
一方で、ラベル不均衡や現代的なデータセットの不足、著作権保護による利用制限という制約があります。  
J-RADはLLMを用いることで、著作権保護されたコンテンツに依存せず、より広範かつラベル均衡なデータセットを提供することを目指しています。

## 引用
研究や論文で本データセットを利用する際は、以下のように引用してください：

```
@dataset{J-RAD,
  author = Say Toaza,
  title = {Japanese Rhetoric Annotation Dataset (J-RAD)},
  year = {2024},
  url = {https://github.com/10sedecim/J-RAD}
}
```

## Contributing
データセットに誤りがある場合や追加を希望される場合は、以下の手順でご協力いただけます：

1. このリポジトリをフォークしてください。
2. 新しいブランチを作成します：
    ```bash
    git checkout -b feature/your-dataset-name
    ```
3. 必要な変更を加え、コミットします：
    ```bash
    git commit -m "Add your dataset description"
    ```
4. ブランチをリモートリポジトリにプッシュします：
    ```bash
    git push origin feature/your-dataset-name
    ```
5. プルリクエストを作成します。

貢献いただく際には、変更内容を具体的に説明してください。  
また、新しい修辞法を追加する場合は、`rhetorical_devices.py` ファイルにその説明を追記してください。

## お問い合わせ
データセットに関する質問やコメントがありましたら、以下の連絡先までお問い合わせください：

[@10sedecim](https://x.com/10sedecim)