![logo](https://user-images.githubusercontent.com/102009707/187976345-7be6f134-113f-4def-9b97-e46bfe86c330.png)

## 📺 K-drama Project
#### 사물인식기능을 활용하여 유저의 찜드라마 태그들을 토대로 비슷한 장르의 드라마들을 추천해주는 사이트

## 목표
-   사물인식기능 활용하여 추천시스템 만들기
-   GitHub 활용 및 효율적인 분업
-   Django를 활용하여 실력 높이기

## 개발 기간
-   06.02.22 ~ 06.14.22

## 멤버구성 & 파트분배
-   <a href="https://github.com/DingoFreestyle"><img 
          src="http://img.shields.io/badge/-Git%20Hub-010000?style=flat&logo=github&link=https://alpox.kr"
          style="height : auto; margin-left : 10px; margin-right : 10px;"/></a> 이호빈 -> frontend, 발표 및 영상제작
-   <a href="https://github.com/Moonmooj"><img 
          src="http://img.shields.io/badge/-Git%20Hub-010000?style=flat&logo=github&link=https://alpox.kr"
          style="height : auto; margin-left : 10px; margin-right : 10px;"/></a> 문명주 -> backend,frontend
-   <a href="https://github.com/woojin9606"><img 
          src="http://img.shields.io/badge/-Git%20Hub-010000?style=flat&logo=github&link=https://alpox.kr"
          style="height : auto; margin-left : 10px; margin-right : 10px;"/></a> 백우진 -> backend
-   <a href="https://github.com/attabooi"><img 
          src="http://img.shields.io/badge/-Git%20Hub-010000?style=flat&logo=github&link=https://alpox.kr"
          style="height : auto; margin-left : 10px; margin-right : 10px;"/></a> 최준헌 -> 사물인식기능, backend
          
## 적용
<img alt="Html" src ="https://img.shields.io/badge/HTML5-E34F26.svg?&style=for-the-badge&logo=HTML5&logoColor=white"/> <img alt="Css" src ="https://img.shields.io/badge/CSS3-1572B6.svg?&style=for-the-badge&logo=CSS3&logoColor=white"/> <img alt="JavaScript" src ="https://img.shields.io/badge/JavaScriipt-F7DF1E.svg?&style=for-the-badge&logo=JavaScript&logoColor=black"/> <img alt="Python" src ="https://img.shields.io/badge/Python-3776AB.svg?&style=for-the-badge&logo=Python&logoColor=white"/> <img alt="Django" src ="https://img.shields.io/badge/Django-E34F30.svg?&style=for-the-badge&logo=Django&logoColor=white"/> <img alt="MongoDB" src ="https://img.shields.io/badge/MongoDB-3DDC84.svg?&style=for-the-badge&logo=MongoDB&logoColor=black"/> <img alt="Figma" src ="https://img.shields.io/badge/Figma-6F6EAE.svg?&style=for-the-badge&logo=Figma&logoColor=black"/>

## 소통
<img alt="Slack" src ="https://img.shields.io/badge/Slack-8A576D.svg?&style=for-the-badge&logo=Slack&logoColor=black"/>

## API
![image (1)](https://user-images.githubusercontent.com/102009707/187976824-47d6d6b1-e159-4848-a14f-7918de894420.png)

## ERD
![KakaoTalk_20220602_193611357](https://user-images.githubusercontent.com/102009707/173728790-8527725e-d02c-4ec1-8062-d13876804897.png)

## Figma Mock-up
![이미지 228](https://user-images.githubusercontent.com/102009707/173729338-1826902a-a711-479b-820d-8f2fddea5bb0.png)

## 구현 기능
### signin.html<br>
![이미지 207](https://user-images.githubusercontent.com/102009707/187977150-13028915-b6d2-41b1-a34d-6151ba9cf03a.png)
<br>
1. 로그인 기능 
2. 회원가입페이지 및 메인페이지 이동
<br>

### signup.html<br>
![이미지 206](https://user-images.githubusercontent.com/102009707/187977297-9c17669a-bf93-4c74-a57c-2fdebcc427c2.png)
<br>
1. 회원가입기능
2. 회원가입완료시 로그인페이지 이동
<br>

### main.html<br>
![이미지 208](https://user-images.githubusercontent.com/102009707/187977411-a9b0b7ef-2d65-4579-8c98-ae9f654d85ee.png)
![이미지 221](https://user-images.githubusercontent.com/102009707/187977443-d2149a6e-e96d-488f-a532-0a871d2c0bd5.png)
![이미지 222](https://user-images.githubusercontent.com/102009707/187977455-08a2f24f-3c67-4bad-b8d3-f226988c7df6.png)
![이미지 214](https://user-images.githubusercontent.com/102009707/187977484-09994cbd-21d0-4a04-8f49-a0eb9fcab8a2.png)
<br>
1. 검색기능
2. 로그아웃기능
3. 추천기능
4. 각 드라마 상세페이지 이동
<br>

### detail.html<br>
![이미지 216](https://user-images.githubusercontent.com/102009707/187977586-ae332c7e-0c09-4b7c-8a7a-4329ade77d46.png)
![이미지 217](https://user-images.githubusercontent.com/102009707/187977598-3f65ae46-0723-447c-a42f-0965e188097c.png)
<br>
1. 댓글 및 별점 포스팅 및 리스팅
2. 관련 추천 드라마 상세페이지 이동
<br>

### like.html<br>
![이미지 218](https://user-images.githubusercontent.com/102009707/187978074-34a680bd-77b6-4536-9f2f-f3a9ee593542.png)
<br>
1. 찜한 드라마 리스팅
<br>

### tag_with_post.html<br>
![이미지 219](https://user-images.githubusercontent.com/102009707/187978596-374a2cca-1d22-4269-854d-04fc053b8e4f.png)
<br>
1. 모든태그 정렬 리스팅
<br>

### tag_cloud_view.html<br>
![이미지 220](https://user-images.githubusercontent.com/102009707/187978411-fd3d3a7c-0dc0-4ce0-9daa-0f290f97ee0f.png)
<br>
1. 태그관련 드라마들 리스팅
<br>

## 👀 기능구현동영상
[![IMAGE ALT TEXT HERE](https://iboxcomein.com/wp-content/uploads/2021/08/%EC%9C%A0%ED%8A%9C%EB%B8%8C_%EB%A1%9C%EA%B3%A0.png)](https://www.youtube.com/watch?v=SqhBUMCGEAU)



