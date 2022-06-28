'''
csv 읽어오기 : read_csv -> to_dict
- pandas.read_csv("파일경로")
파일값 불러오기
- data_value = .to_dict(orient="records")

파일 저장하기 : dict -> dataframe 변환 -> to_csv
- pandas.DataFrame(data_value)
csv로 저장(단, 지속적으로 저장시 index 계속 추가되므로 삭제)
- .to_csv("data/words_to_learn.csv", index=False)
'''
