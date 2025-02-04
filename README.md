# Japanese Rhetoric Annotation Dataset (J-RAD)

This project is available in multiple languages:
- [English](README.md)
- [日本語](README.ja.md)

## Overview
The **Japanese Rhetoric Annotation Dataset (J-RAD)** is a dataset of Japanese texts annotated with rhetorical devices. This dataset is originally designed for analyzing rhetorical devices in Japanese stylistics and stylometry. J-RAD provides text data with rhetorical devices, automatically generated by large language models (LLMs).

## Background
In the analysis of Japanese stylistics and stylometry, examining rhetorical devices is essential, yet there has been a lack of comprehensive datasets focusing on these devices. Additionally, annotating rhetorical devices in existing novels presents challenges such as label imbalance and copyright restrictions. J-RAD addresses these issues by using LLMs to automatically generate texts incorporating rhetorical devices.

## Dataset Structure
- `data/raw`
  - [`single_rhetorical_device`](./data/raw/single_rhetorical_device):  
    Contains texts that use only one rhetorical device. Each rhetorical device is stored in a separate JSON file, with each file containing 500 texts.
  - [`multiple_rhetorical_devices`](./data/raw/multiple_rhetorical_devices):  
    Contains texts that use multiple rhetorical devices randomly. The data is divided into JSON files, each containing 1,000 samples, with a total of 100,000 texts.

- Metadata
  - [`scripts/rhetorical_devices.py`](./scripts/rhetorical_devices.py):  
    Lists the types and descriptions of rhetorical devices. The current version includes 153 types of rhetorical devices.
  - [`./metadata/rhetorical_device_counts.csv`](./metadata/rhetorical_device_counts.csv):  
    Provides statistics for the entire dataset. The current version includes a total of 444,652 rhetorical devices.

## Sample
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
([View full sample](./data/sample/samples.json))

## License
J-RAD is released under the CC BY-NC-SA 4.0 license.  
Cannot be used for commercial purposes. For non-commercial purposes, it can be freely used with appropriate credit.

## Previous Research
A related dataset to J-RAD is [J-FIG](https://www.kotorica.net/j-fig/info/guideline).  
J-FIG is a dataset with rhetorical device annotations on actual Japanese texts and is more natural than J-RAD.  
However, it faces constraints such as label imbalance, lack of modern data, and usage restrictions due to copyright protection.  
By using LLMs, J-RAD aims to provide a more extensive and balanced dataset without relying on copyrighted content.

## Citation
If you use this dataset in your research or paper, please cite it as follows:

```
@dataset{J-RAD,
  author = Say Toaza,
  title = {Japanese Rhetoric Annotation Dataset (J-RAD)},
  year = {2024},
  url = {https://github.com/10sedecim/J-RAD}
}
```

## Contributing
If you find any errors in the dataset or wish to make additions, you can contribute by following steps:

1. Fork this repository.
2. Create a new branch:
    ```bash
    git checkout -b feature/your-dataset-name
    ```
3. Make the necessary changes and commit them:
    ```bash
    git commit -m "Add your dataset description"
    ```
4. Push the branch to the remote repository:
    ```bash
    git push origin feature/your-dataset-name
    ```
5. Create a pull request.

When contributing, please describe the changes you have made in detail.  
If you are adding a new rhetorical device, please also add its description to the `rhetorical_devices.py` file.

## Contact
If you have any questions or comments about the dataset, please contact:

[@10sedecim](https://x.com/10sedecim)