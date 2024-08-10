# api이해하기 
# interface - 2개의 시스템이 상호작용할 수 있도록 접속되는 경계 ex) 식당갔을때 1.종업원에게 직업 주문 2.키오스크 주문 3.종업원이 오는 방식 
# 처럼 이런 각각의 주문방식을 interface라고 생각
#  1번의 주문방식인데 2번으로 하면 에러가 뜨는거랑 같다
#  api는 서비스의 요청과 응답에 대한 규칙을 의마하지만 보통 api라고 하면 이러한 요청과 응답을 처리하는 서비스(기능)을 의미한다.
#  요청과 응답 이라는 개념이 중요함
#  프레임워크 와 라이브러리 차이점 
#  프레임워크 - 정해진 룰에 맞게 적용을해야 사용 - 조금더 제한된 - 프레임워크는 항상 공식문서를 한번 확인해보자
#  라이브러리 - 개발자가 자유도 높게 가져다 쓸수있는 

from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def sayHello():
    return {"message": "안녕하세요"}
# uvicorn mainAPI:app --reload 하고 서버 접속해서 http://127.0.0.1:8000/hello
# 로 들어가면 내가 보낸 메세지(응답)을 볼수있다
# http://127.0.0.1:8000/docs 로 들어가면 api의 서버에 어떤 api들이 제공 되어있는지 보인다

@app.get("/")
def sayWelcome():
    return {"message": "환영합니다"}