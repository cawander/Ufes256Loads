import streamlit as st
import pandas as pd
#import ufes_256_load
import numpy as np
import io
import base64
import requests
from io import BytesIO
import zipfile

TOTAL_ROWS = 999601
LINK_DOWNLOAD_DATASET = 'https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/rz3fr95t2s-1.zip'

LINK_CARGA = [
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/244308ed-f5ff-4e0f-8d8e-be34517bfcc2/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/c65be17c-080c-4736-921f-21346fec1b56/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/2237788f-fec9-4313-96de-40628629bc41/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/4702d751-50ef-4085-a530-2a8762115f5c/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/98e7c560-0b8d-491d-8691-b248f551b7c3/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/2c0af617-9814-4db6-84ae-7c30c0789af8/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/531c9bb4-a2fb-49dc-88d1-16f0b76fc4c9/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/4430ef93-43a9-4c86-afcf-378625f11f33/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/68d652d1-9c2d-4a7f-abc3-73aba45a68bf/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/af0d6985-394a-46df-9bc6-f2bbebbf20fd/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/869d2589-3767-44c3-906f-b6cfa35ee41d/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/1fa353aa-8ab0-474d-8426-5ab9a4897a4e/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/6bedf1ad-5b4d-40e0-98b2-1d446d2bc3d2/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/49f0e68e-0c35-4d66-ada2-a7246b810e86/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/e14915c1-ab31-485b-a9d8-757ed8308685/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/3e5d53a6-5f3d-42e1-a589-eee42a06e7e2/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/113e291a-d7f6-4186-ac7a-a1a8e3e06e03/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/8ec44c3b-b159-4d9c-828c-82b808953cda/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/71a69c68-09b2-4e05-a841-5276650d07fc/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/beb83081-a82b-4222-8849-8641a9c77168/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/2c7463cc-4374-4cec-a1ae-b63c279f5123/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/f50afbb3-459f-4c5e-bf7c-d4e23ee48c11/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/9eebe876-a0f9-42d9-b8c3-0c66925b37cb/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/509b023c-6882-4bbf-828c-bf57a399e6e8/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/a955f630-996d-49e1-b5f2-775ec22404c3/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/9fa8c55d-253f-486d-a09c-05323b656534/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/6b980e7f-9355-4e43-a3e8-01f85570d8ec/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/1898880b-e283-4b80-bb19-3d2e8934db28/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/26b570fa-57ad-4929-922f-916cd10cb9b6/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/1a9ac3c5-9395-404a-858b-0337499f97ab/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/d343dd80-bede-4a6b-b1eb-a4c0cdf23978/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/0489ae9f-6bdd-4e4e-b6a1-cdd7163cf912/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/f4ea7910-74fa-4a83-914b-c0d1518519f0/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/380e466b-a9fd-4a5f-b68b-f1a66cc87e17/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/47b6cdd8-aaaa-43b5-b56c-d77ad05b0014/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/cbe62f6c-3118-4a9b-b5e6-dbb8164ee2fe/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/6faea281-2e50-4eb1-9e6d-75e59c8df5f0/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/9cf46fd5-2901-406b-926c-d5c724e715e1/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/466198b0-b667-4a05-b848-68a4f9ef3c39/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/25f7e524-3856-4661-8614-770cfa54405b/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/f01342d3-a2b7-4d4e-b99d-9332a195c383/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/fb021166-7d34-4c8b-b425-e6ed30cb1f7e/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/f7d36bfa-0c6f-4aca-89f0-d1920745bf6d/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/bcdc41f8-140e-4f1e-904e-28f6b2ce7878/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/62ac089c-d00d-4b07-afe9-717490c65814/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/ce3f2450-719d-4165-9ffd-73e2e66e8abc/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/0b0faeff-8d45-4e6a-aa83-824ddddeef9a/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/7985ab34-7282-4726-935f-8aecc17f842a/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/f3884891-d7cd-4926-9c75-bc0ca0888947/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/6d5ed4d6-6625-4d8f-8286-d82aad4d921b/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/04f6e3cb-6947-4d8d-9a93-a1c86f45fe7f/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/407b2476-1fb2-497b-97a2-918473fe7e1c/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/bd5636e5-e100-41cc-967e-6e78bf6f150b/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/1d339f23-ab4a-40e9-a286-48faecdba039/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/5b602b20-fe52-4fc6-a17c-a194f50343d7/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/7dfe703e-19af-4f9a-b242-648ed0679782/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/ac92788d-7eec-40bc-8d32-c944106eac42/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/8d291acf-0781-45d4-b847-8c2aac60a792/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/a107d2dd-7e76-4134-af5b-b0accc9a2f39/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/62b37563-4eb5-481d-85c5-c818a8748f56/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/4bd579e7-c13d-4778-9246-da53b95c8ff1/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/fcb327a8-f852-4750-835b-41e2ea74b3de/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/f6fd1e9a-1862-4b70-851e-cd3ea147679d/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/c2ec203a-9d09-4094-8025-6b29a0e6d21e/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/ccfa2ebf-076e-4a67-96c7-d0108b5d0b18/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/3b4ef16d-4588-4d01-bf0c-c4bf9eaa8168/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/8d399b4c-32dc-4257-b7c0-3c3ded2e1d1f/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/2e9b331c-1ab8-4dc9-9c4e-6c75de5e40fb/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/1def8700-60e4-4e6c-aa01-43af9e3c3896/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/98911dd3-74ed-4d13-a0f9-9e86594fed67/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/b10bb9f5-22de-4f85-9140-77dd826e533a/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/1f1e8ae2-cc70-448f-9582-9b5cf038c403/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/abe6db64-2967-4edc-a5ef-cdf075655007/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/077ab8e7-a1c3-45b2-b107-1b94806e572c/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/660a8ea3-a0a5-4e3a-8424-1922d5a25988/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/17cbf1be-92ba-4673-bc89-479a268af9e8/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/39552859-9284-454e-a7b8-95a579e920e1/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/54bde29c-1c0c-4734-84dc-66758c31ee5b/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/25750469-13ed-4b29-8daf-8823a52be7d5/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/441e3d6f-6ddf-4e88-94b9-80c659727bab/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/8111a3c9-b70c-4b60-99da-1e22c2270dba/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/1b5135c6-5d40-47e7-8182-52de5d8dd56f/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/dc65a582-5376-4668-935c-2fd26626e2c4/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/87b942d2-a3ac-4ae5-9aba-5141c739116f/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/d6ef7fb6-69bb-4a2c-ad8c-f64e561e936e/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/24837fd9-e647-472a-9430-0db58789eb60/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/fe24c8b8-8a8b-4b3c-852c-c5d0bfe78056/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/e1a2368f-1640-4ebe-87ef-df15629f47a4/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/fbbe7fb4-a9d9-4fa7-add4-0efca008babd/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/46c36075-2b28-4994-a07d-414821b757b4/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/ff3001ee-f55a-4422-94eb-30e15133449b/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/dfb6c0f9-4f1d-4f80-a6ad-6b8022fec21c/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/dd59b2af-517c-46c7-a8fa-17ed64098e08/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/746f861d-22bd-4e14-9df2-ad15a1eced56/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/9965918b-3d1e-4477-9713-9f9d4c793775/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/7f7d7fb3-5807-4a8d-927a-2ff36f91c06d/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/54042ee1-ec85-448a-beb1-430689af69ca/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/d51079a5-46c4-4780-9b66-775c338187dc/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/f20b6aa1-3250-4559-8002-7b85845130a1/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/67fff419-ef85-4982-bd80-7161c144c626/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/76768fb6-5cfb-439e-8906-b79ddbc24a6a/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/dff1d8d5-e238-429f-aac0-874d9a0ce646/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/f67c221c-176a-49b8-b8b9-b7a4d99316a9/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/f70832db-8a07-4946-8afb-2817d861f3c2/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/5cc7130f-076a-4e48-a785-8cc52871e7d3/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/a6a9c795-0903-4f83-903b-e560583739cf/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/fe21dc7f-ec43-4a79-a1e3-18946fd24d90/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/ee8a7398-628e-4554-9aea-817f9d16fe58/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/9e72563b-1b20-49ae-ba85-35fbca64449a/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/0b0a515b-9b20-4aea-9fb5-ed27c5d8b050/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/e1ec4a2d-60a3-4715-af63-be557c505f61/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/f05a71cc-69d1-4975-855d-a4d49e9cb3c0/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/305a08a8-0d4a-46ad-814e-3cd8260d82b5/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/c42fea29-d679-4957-9a67-d9ddbf1b5b5a/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/256bfd6c-3852-4522-9b29-326705d1d8f2/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/70a757cb-ef89-45db-a642-a2e864491082/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/dabe43c6-c725-44f6-a85b-47e50cde0d20/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/b5885634-1822-4fe6-a0c9-911890d6d047/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/219aa121-d885-44f8-b91e-38cf71f9c38b/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/9ec7b605-eb3c-4e33-831a-d57c4018ae5d/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/287b2c61-6be0-4b4f-9545-0a7a1961badb/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/b1b25897-a1fb-470c-a846-b2c8cba9bbfb/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/0be68a7f-e33b-49f9-8f70-1f1e90b9e11c/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/7ae032bc-9c90-4267-bfc1-f93d9364ea3e/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/03f3fef9-b4ff-4bc4-a832-1ddc89946592/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/3fcabd7f-793c-4b30-8b56-b2a03216ac66/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/f8473455-6329-4b9f-8780-69eec2742492/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/0d6206ca-be96-4e10-b45c-169bd5d32719/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/daf8ee6d-2222-427d-a12b-edf2da7f9d01/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/a354e32a-0abc-4317-9905-2aa4ec1e4ebe/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/1adc0b39-1765-42fc-9793-67968306d8e0/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/4cc5430e-cbd8-4d2f-9138-8ff8e822341b/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/35134e80-f845-4fd9-ad45-7e63596596cd/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/5e638f25-4c13-4763-a99c-c359109cc102/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/fe7ea164-6041-4a1a-9d75-a19628d2770c/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/82c600c8-b05a-4457-9790-414905311a2e/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/87e836e2-d920-42ab-98b5-14eef9fcad3b/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/6cade60c-669e-4cc2-a0fe-dc6b7b617840/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/133992d0-0b61-4ad7-a945-c327ffe39c8e/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/5621868d-8527-488b-9d4d-bffa28341bf5/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/8ab2f86b-0aa5-4ca0-8a18-baae54ffd28d/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/49dee3d0-41c4-47ea-8666-8f609fbc2e16/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/22a7b6f6-dca3-47b9-a7eb-e44e609678b4/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/8d537e27-8c6e-4572-867d-ad06bcbd42ae/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/c7091f90-6488-494e-976c-6bd4bdf1c397/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/fcc0f693-15a1-4f0e-9c39-0ffe6786cd59/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/4ea92646-fdff-4260-856f-46f3905dfbc8/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/6daa863a-6f46-4b18-8774-c1604c34dc79/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/945b1500-0cc5-4c1d-8fcc-bb767422040b/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/f0471f5b-3756-4f65-b88e-db308815b0ea/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/bf2be8d4-7acd-4206-99f9-bbef1219175f/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/0e750cec-1223-4866-8be8-4ec44f4dd102/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/556e899c-7757-45c7-9f10-2c43cc62f33a/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/f85522c6-29f4-420c-aa45-4f6e20a220cd/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/36925f8a-6848-4ff7-b618-3994870eb848/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/8f419e26-0ffa-4c9c-88c1-49d4ce51a9f2/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/c19e38db-f05d-4c95-b216-7171b10623e2/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/48f8a8f8-d1d0-4a84-8979-72d9fd6e5074/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/a7394f19-68f7-4212-a1f6-924fc2dfaf47/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/21b1871a-ad61-4e25-9199-02bcdc193f60/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/5cada3a0-eea2-40c6-8f67-056b1b104ce0/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/1357daeb-a99b-4022-8bae-9397a8ce1e38/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/84014236-7ce6-44e1-9ed3-b3ee41f9b5bf/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/bd35e77f-09e6-4e16-bdb6-e3e7a46c3177/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/6870b1b2-1e50-4613-a426-cb746ea573c7/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/b66e40b8-7381-462f-90e9-ec9fc8c13bc0/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/01653106-f7b2-465e-8f11-c4629ece8eb2/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/1c92d7bc-2dab-4759-b611-b2031cc6671c/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/5da719e3-5d2e-49e8-b647-737a03201685/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/687809cf-096a-476f-8f3a-7758fca14d22/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/8fa74ef9-11bf-4191-a55c-d28a2341bd4f/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/5791a423-1763-4753-ad85-8db2dacc63f7/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/12bf5ea6-1a6c-4d71-87f9-75930e2740af/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/80499fa5-2a52-45cb-9ab6-5b148e7dfb57/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/43a5b974-8741-4551-8c66-114505d58804/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/4f2dda4b-a1a3-4778-a435-43093194e019/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/22808f0e-a321-4a4b-ac84-d78feadc1e17/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/63139e43-a1fa-4fe5-9d5e-cee8bb0e40c2/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/82685f29-a5e2-471c-a0ba-fd0c4e1f675e/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/b41410a5-7210-48f5-9bc9-d705f79bdfa0/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/60b969ec-bdb8-401c-bd59-2d426089cad7/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/833b12ea-da62-4344-a289-05b040deb69d/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/3c5aaf82-680a-4012-b2da-011af10cc41e/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/74b9f6ff-7d1b-4c70-8464-85c300f9156e/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/2a733351-1adb-4760-8c02-51d4b9ce8cd0/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/7cf8a648-186f-47eb-b2e2-d37a22c417a2/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/ce97c379-0aa0-41f7-9206-509674c652bf/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/5218c1e1-8038-4878-ac2c-0f0123c88d5f/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/4d7df612-3ad5-4838-b95a-7d44b21f840d/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/047fc926-13c3-481a-a482-deaf1dbea279/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/60916786-3b06-4df1-9a77-763d44016322/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/be53cd06-cece-4080-8df1-da68318515ef/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/493cafe4-9222-4356-9d1e-2cea38d82a2a/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/1ade19dc-9061-41c0-b35b-82fa1c76406b/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/a9ea1d4b-bfea-485e-b5a7-bb75c9cfbaf1/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/c55028c3-70f2-454e-aea8-32178b3925aa/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/6403a1ef-ffd2-4b54-9fbb-01bcf01eeca2/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/55e9021f-6ac1-4492-986f-22f9ba7341c6/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/e4ca3a19-3227-467f-aaa3-4b326ec86c6b/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/902a6763-c673-40c9-91d1-9b8a5fdc3f3b/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/d36669f5-2fe2-4e87-b06d-cfa1e8355adf/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/baf30c41-64a9-40fc-a12c-6d1555a5674a/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/c4a62ea5-ac06-4199-b9f2-2fa5799c49af/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/3920f74f-66ac-4b33-b053-4b9b39a3c631/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/4f857fc1-4ecc-4eeb-8880-f3a54104b194/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/8484e537-d683-4e2c-919d-c182a97ca51c/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/4da26dd2-03d8-4204-9f2f-4d690ea75d55/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/55d4b1c3-36fb-408b-8fe4-0c5cfc84a077/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/6f9b0ee0-c2d4-4f98-a93e-bf20f2ce14f8/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/263d7782-24bd-46e5-a859-4d4556dc6db0/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/cbc262ff-8a58-426d-887a-65e4665ef877/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/48deb017-aae9-4a7f-8b48-5a760cfc12a7/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/c846f559-89d6-4058-9232-27b24da0c717/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/6c6e5037-dc37-47eb-a8ff-06e79512ac3a/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/96da7d52-efda-4d6f-a0f1-bfda6f9d797f/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/3fec8f24-1c80-44ef-af50-f4a348128e57/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/f69d76fc-b128-48c2-8045-4ea2e1ca6d39/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/0712d1b2-2225-4944-a5c0-11b2c52449d9/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/5046e954-4106-4017-8612-ef8bee2bf2a3/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/a1bb1f17-a9a2-4c10-80d0-9428fa517e26/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/9a95b786-9665-4092-bb27-17d45b1c34eb/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/ec1b12ae-f539-466e-b1fa-7533e2d4c2dd/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/05aeaadd-5c73-47b3-90c3-fb5aae567434/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/8320ce16-cf47-4901-afb4-f398e13cae64/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/78be955c-01fb-43a1-9321-0836dba2d032/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/896789bd-4b5f-4a3b-85bb-8afcfe00b82a/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/e3471821-deea-4fef-a606-540901e74765/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/28ffae2b-5bd5-40f4-ae47-21c176b2e1c4/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/09619f5d-af0b-4f21-8ee1-0eddef04aec5/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/8b748d6e-b8e4-439e-9c5f-84bc7771c5c9/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/e9885f26-0fa7-444c-8d05-e3192ab3278c/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/3ac8db04-e3d3-4207-9685-efb43203a161/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/1c9d1516-dd28-4b6a-aa9e-8a661f0fabdc/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/747db65d-8f17-41f3-a948-273126d32618/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/861e55b6-2533-416f-a419-fded9ec0976f/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/04b718ee-8bf4-4f42-b339-535d6219a9a9/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/b2bb3a95-9fbb-4236-ae83-761006fc0c0e/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/77abdf97-1cf3-4b3d-a262-fd93a419d300/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/80bdf963-28f7-46ac-8a66-2df9ee7dbc17/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/d635b8bb-a77d-481d-8911-b0ad13dc80f5/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/02822f53-74b4-4c76-8596-d5dc07b5dfd0/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/0aa70c2b-e869-4383-9201-44b9f2befd1a/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/de27f391-5c68-4b8d-9ae3-c22852b9407c/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/2a702c95-3462-46da-a867-322ccbee3ee9/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/996c7977-3f9d-4283-9bf8-5474f918d168/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/61790ad5-c2d4-4d1a-85bf-c5d673cd54fe/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/37d1dc02-6b5c-4516-bf15-18525a1505d3/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/c94a8523-b8c2-4456-bcfd-d8fd4b832877/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/4b53854e-ef37-49e6-a322-dea537b255dc/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/659c6e10-83b5-4d5e-acf5-473abd853d9b/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/211eee04-3edf-4130-94cc-b6012fdc2eda/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/7fd4dce4-b4c7-47fb-8102-d3995ea598a9/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/cde5d321-5300-44ca-90f8-595130bca6bd/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/4f20f7b8-97bb-449f-83ab-ca5c5a194ba9/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/60fa5f2a-9b30-4956-abd0-ec1ed02adbd9/file_downloaded',
    'https://data.mendeley.com/public-files/datasets/rz3fr95t2s/files/40f98965-5fde-4902-bc41-ca5183f4d0b5/file_downloaded',
]

# streamlit run my_app.py
st.set_page_config(
    page_title="Ufes: 256_Loads",
    layout="wide",  # Define o layout para ocupar toda a largura da página
)

@st.cache_data
def download_dados(link_carga):
    # tabela = pd.read_csv("resultados.csv")
    # return tabela

    # Realizar o download do arquivo
    #response = requests.get(LINK_DOWNLOAD_DATASET)
    response = requests.get(link_carga)
    return response

def buscar_dados(cod_carga, percentual_amostras):

    print('LINK_CARGA = ', len(LINK_CARGA))

    #A opção vai ficar indisponível por hora.
    use_cache_memory = False

    response = None
    if use_cache_memory:
        response = download_dados(LINK_CARGA[cod_carga])
    else:
        response = requests.get(LINK_CARGA[cod_carga])

    # Abre o arquivo ZIP
    with zipfile.ZipFile(BytesIO(response.content), 'r') as zip_ref:
        # Lê o conteúdo do arquivo CSV no arquivo ZIP

        print('Conteúdo do zip: ', zip_ref.namelist())

        nome_arquivo_csv = f'L{cod_carga}.csv'
        print('nome_arquivo_csv: ', nome_arquivo_csv)

        with zip_ref.open(nome_arquivo_csv) as file:
            nrows = int(TOTAL_ROWS * percentual_amostras / 100)  # Calcula o número relativo de linhas a serem lidas

            # Converte o conteúdo do arquivo para um DataFrame do pandas
            df = pd.read_csv(file,  nrows=nrows, skiprows=1)

            # # Elimina a primeira linha do DataFrame
            # df = df.drop(index=0).reset_index(drop=True)

            print('Dataframe: ', df.head())

            return df

# Função para traduzir textos
def translate_text(text, lang):
    translations = {
        'pt': {
            'load_dataset': 'Dataset de 256 cargas',
            'team_presentation': 'Grupo de Pesquisa sobre Tecnologias Voltadas a Smart Grid \nUniversidade Federal do Espírito Santo',
            'dashboard': 'Dashboard de Dataset de 256 cargas',
            'presentation': 'Apresentação de dataset contendo sinais elétricos de 256 cargas referentes a combinações entre 8 equipamentos eletroeletrônicos alimentados a partir de um ponto de acomplamento comum.',
            'download_dataset': '[Clique aqui](https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/rz3fr95t2s-2.zip) para baixar o dataset. Descrições atualizadas sobre o dataset são publicadas [aqui.](https://data.mendeley.com/datasets/rz3fr95t2s)',
            'select_load': 'Selecione a carga',
            'load_formation_details': 'Detalhes de formação das cargas',
            'current': 'Corrente [A]',
            'voltage': 'Tensão [V]',
            'percentage_samples': 'Percentual de amostras',
            'filename_xlsx': 'Detalhes_Dataset_256_cargas'
        },
        'en': {
            'load_dataset': '256 Loads Dataset',
            'team_presentation': 'Research Group on Technologies for Smart Grids \nFederal University of Espírito Santo',
            'dashboard': 'Dataset Dashboard of 256 Loads',
            'presentation': 'Presentation of a dataset containing electrical signals from 256 loads corresponding to combinations of 8 electro-electronic devices powered from a common coupling point.',
            'download_dataset': '[Click here](https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/rz3fr95t2s-1.zip) to download the dataset. Updated descriptions about the dataset are published [here.](https://data.mendeley.com/datasets/rz3fr95t2s/1)',
            'select_load': 'Select the load',
            'load_formation_details': 'Load Formation Details',
            'current': 'Current [A]',
            'voltage': 'Voltage [V]',
            'percentage_samples': 'Percentage of samples',
            'filename_xlsx': 'Details_Dataset_256_loads',
        },
        'es': {
            'load_dataset': 'Conjunto de datos de 256 cargas',
            'team_presentation': 'Grupo de Investigación sobre Tecnologías para Redes Inteligentes \nUniversidad Federal de Espírito Santo',
            'dashboard': 'Tablero del Conjunto de Datos de 256 Cargas',
            'presentation': 'Presentación de un conjunto de datos que contiene señales eléctricas de 256 cargas correspondientes a combinaciones de 8 dispositivos electroelectrónicos alimentados desde un punto de acoplamiento común.',
            'download_dataset': '[Haga clic aquí](https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/rz3fr95t2s-1.zip) para descargar el conjunto de datos. Las descripciones actualizadas sobre el conjunto de datos se publican [aquí.](https://data.mendeley.com/datasets/rz3fr95t2s/1)',
            'select_load': 'Seleccione la carga',
            'load_formation_details': 'Detalles de formación de cargas',
            'current': 'Corriente [A]',
            'voltage': 'Voltaje [V]',
            'percentage_samples': 'Porcentaje de muestras',
            'filename_xlsx': 'Detalles_Conjunto_datos_256_cargas'
        }
    }
    return translations[lang][text]

# Iniciar sessão do Streamlit
session_state = st.session_state

# Definir o idioma padrão como português
if 'lang' not in session_state:
    session_state.lang = 'pt'

# Adicionar uma opção para escolher o idioma no canto superior direito da barra lateral
selected_lang = st.sidebar.radio("Choose Language", ["Português", "English", "Español"])

# Atualizar o idioma se a seleção do usuário mudar
if selected_lang == "Português":
    session_state.lang = 'pt'
elif selected_lang == "English":
    session_state.lang = 'en'
else:
    session_state.lang = 'es'

with st.container():
    st.subheader(translate_text('team_presentation', session_state.lang), divider='rainbow')
    #st.subheader(translate_text('load_dataset', session_state.lang))
    st.subheader(translate_text('dashboard', session_state.lang))
    st.write(translate_text('presentation', session_state.lang))
    st.write(translate_text('download_dataset', session_state.lang))

def display_image_and_download_button(image_path):

    # Lê o conteúdo do arquivo
    with io.open("Detalhes_Dataset_256_cargas.xlsx", "rb") as file:
        file_data = file.read()

    # Codifica o arquivo em base64
    file_data_base64 = base64.b64encode(file_data).decode('utf-8')

    # Exibe a imagem
    st.image(image_path, use_column_width=True)

    # Exibe o botão de download oculto
    # st.markdown(
    #     f'<a href="data:application/octet-stream;base64,{file_data_base64}" '
    #     f'download="Detalhes_Dataset_256_cargas.xlsx" id="download_button">{translate_text("load_formation_details", session_state.lang)}</a>',
    #     unsafe_allow_html=True
    # )

    st.markdown(
        f'<a href="data:application/octet-stream;base64,{file_data_base64}" '
        f'download={translate_text("filename_xlsx", session_state.lang)} id="download_button">{translate_text("load_formation_details", session_state.lang)}</a>',
        unsafe_allow_html=True
    )

# Crie uma coluna de layout usando st.columns
col1, col2 = st.columns(2)

# Adicione a figura ou qualquer outro conteúdo à coluna à direita (col2)
with col1:
    container_col1 = st.container()

    # Lista de opções para o selectbox
    opcoes = list(range(256))  # Valores de 0 a 255
    valor_padrao = 255

    cod_carga = st.selectbox(translate_text('select_load', session_state.lang), opcoes, index=opcoes.index(valor_padrao))

    # Centralize verticalmente o conteúdo dentro de container_col1
    st.markdown(
        """
        <style>
        .st-eg {
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100%;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # st.image(f"figuras/F{cod_carga}.png", use_column_width=True)  # Substitua "sua_imagem.png" pelo caminho da sua imagemimage("F256.png", use_column_width=True)  # Substitua "sua_imagem.png" pelo caminho da sua image
    #

    # Caminho da imagem
    imagem_path = f"figuras/F{cod_carga}.png"

    # Exibe a imagem e um botão para download
    display_image_and_download_button(imagem_path)

# Adicione o gráfico de linha superior (subcol1)
with col2:
    # Adicione um container para a col2
    container_col2 = st.container()
    # cod_carga = st.selectbox("", list(range(256)))

    # Percentual de amostras
    percentual = st.slider(translate_text('percentage_samples', session_state.lang), min_value=0, max_value=100, value=1)

    # # Caminho para o arquivo zip
    caminho_zip = r'C:\Users\cawan\OneDrive - Universidade Federal do Espírito Santo\Projetos_Python\UFES_NILM_Dataset_256_Load\dataset_256_loads.zip'

    # # Nome do arquivo CSV específico que você deseja extrair
    nome_arquivo_especifico = f'csv/L{cod_carga}.csv'

    #dados = ufes_256_load.buscar_dados(caminho_zip, nome_arquivo_especifico, percentual_amostras=percentual)
    #dados = buscar_dados(nome_arquivo_especifico, percentual_amostras=percentual)
    dados = buscar_dados(cod_carga, percentual_amostras=percentual)

    # Adiciona um índice numérico ao DataFrame
    dados = dados.reset_index()

    print('Dados:', dados.head())

    #Calibração
    # Vmax = dados['voltage'].max()
    # Imax = dados['current'].max()
    dados['index'] = dados['index']/99960
    dados['voltage'] = dados['voltage'] * 126.5 * np.sqrt(2)/1.37

    #dados['current'] = dados['current'] / 993

    # print(dados.head())  # Exibir as primeiras linhas do DataFrame
    # print(dados.columns)  # Exibir os nomes das colunas no DataFrame

    with st.container():
        st.markdown("###### " + translate_text("current", session_state.lang))
        st.line_chart(dados.set_index("index")[["current"]])

    with st.container():
        st.markdown("###### " + translate_text("voltage", session_state.lang))
        st.line_chart(dados.set_index("index")[["voltage"]])

# Ajuste a altura dos containers
container_col1.height = 400  # ajuste conforme necessário
container_col2.height = 400  # ajuste conforme necessário
