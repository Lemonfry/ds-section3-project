# ds-section3-project
Codestates AI-07 Section 3 Project

**심장병 환자들의 생활 습관 데이터를 기반으로 하는 심장질환 예측 모델**

데이터셋 : kaggle의 심장질환 데이터인 Heart Disease Health Indicators Dataset으로, 미국 CDC(질병통제예방센터)에서 2015년 실시한 설문조사 기반 데이터

프로젝트 진행 방법(visual stuido code에서 진행했습니다)
1. 심장병 질환자 데이터 전처리 및 mongodb로 전송(dropna.py, importdb.py)
2. 데이터를 기반으로 심장병 가능성을 분류하는 Machine Learning 모델 제작(가능성 높음/낮음의 2단계)(ml.py, xgbc.pkl)
3. Flask를 통해 모델 input을 받아들이는 사이트 제작(templates 폴더 home.html, after.html)
4. Pickle 파일을 이용해서 3번의 사이트에서 input을 받으면 예측을 다음 페이지에서 보여주도록 설정(app.py)
