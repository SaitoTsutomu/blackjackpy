# MkDocsについて

MkDocsは、ドキュメント作成のツールです。

* ドキュメントはマークダウンで書く  
* Pythonのdocstringからマニュアルを自動生成する

[https://www.mkdocs.org/](https://www.mkdocs.org/) 本家  
[https://mkdocstrings.github.io/](https://mkdocstrings.github.io/) 拡張機能

有名どころで使われています。  
 [Ansible](https://molecule.readthedocs.io/configuration/), [Apache](https://streampipes.apache.org/docs/docs/python/latest/reference/client/client/), [FastAPI](https://fastapi.tiangolo.com/reference/fastapi/), [Google](https://docs.kidger.site/jaxtyping/api/runtime-type-checking/), [Jitsi](https://jitsi.github.io/jiwer/reference/alignment/), [Microsoft](https://microsoft.github.io/presidio/api/analyzer_python/), [Prefect](https://docs.prefect.io/2.10.12/api-ref/prefect/agent/), [Pydantic](https://docs.pydantic.dev/dev-v2/api/main/), [and more...](https://github.com/mkdocstrings/mkdocstrings/network/dependents)

## 利用例

サンプルのリポジトリ（ハノイの塔）  
[https://github.com/SaitoTsutomu/k-peg-hanoi](https://github.com/SaitoTsutomu/k-peg-hanoi) 

ドキュメントを作成するために今回、作成・修正したファイル。

* mkdocs.yml: ドキュメントの設定ファイル [サンプル](https://github.com/SaitoTsutomu/k-peg-hanoi/blob/master/mkdocs.yml)  
* docs/index.md: ドキュメントのトップページ [サンプル](https://raw.githubusercontent.com/SaitoTsutomu/k-peg-hanoi/refs/heads/master/docs/index.md)   
* Pythonのコードにdocstring: [サンプル](https://github.com/SaitoTsutomu/k-peg-hanoi/blob/890b0c1ea123b039de0d80e01213bb1561954bff/src/k_peg_hanoi/__init__.py#L35-L40) 

**docstringの種類**  
[https://mkdocstrings.github.io/python/usage/configuration/docstrings/](https://mkdocstrings.github.io/python/usage/configuration/docstrings/) 

私は、シンプルなsphinxスタイルで書いています。  
VS Codeの [autoDocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) という拡張機能を入れると `”””`で自動で雛形が作成されます。  
スタイルは、設定の`Auto Docstring: Docstring Format`の`sphinx-notypes`を選んでおきます。

## MkDocsのインストール

| `uv tool install mkdocs --with mkdocstrings-python --with mkdocs-material` |
| :------------------------------------------------------------------------- |

※ mkdocsのコマンドが新しい仮想環境にインストールされるので、既存の仮想環境には影響を与えません。

## ドキュメント作成

| `mkdocs build` |
| :------------- |

`site`というフォルダーに作成されます。

## GitHub Pagesで公開

下記のコマンドでGitHub Pagesでマニュアルを公開できます。

| `mkdocs gh-deploy` |
| :----------------- |

サンプルリポジトリ  
[https://saitotsutomu.github.io/k-peg-hanoi/](https://saitotsutomu.github.io/k-peg-hanoi/)   
[https://saitotsutomu.github.io/blackjackpy/](https://saitotsutomu.github.io/blackjackpy/) 

MkDocsの該当マニュアル [https://www.mkdocs.org/user-guide/deploying-your-docs/](https://www.mkdocs.org/user-guide/deploying-your-docs/) 

GitHub Pagesは、公開リポジトリだと無料プランで使えるようです。
