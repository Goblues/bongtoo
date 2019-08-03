# App
> models을 정의할 때  field_name : type = ex) name = modles.charFiled()
## Commons
공통으로 사용하는 모델을 정의하기 위한 앱
### Models
* Activity(봉사활동)
  * name : char
* Subject(봉사대상)
  * name : char
* Region(봉사지역)
  * city : char
  * town : char

### imports
* construct_data  
  commons 데이터 초기화하는 함수
  

## Review
봉사활동 리뷰들을 위한 앱
### Models
* Review(봉사활동 리뷰들)
  * user : foreinkey
  * title : char
  * body : text
  * region : manyToMany(Region)
  * activity : manyToMany(Activity)
  * subject : manyToMany(Subject)
  * create_at : dateTime
  * updated_at : dateTime
  * get_thumnael : def
  * like_count : def
* Comment(댓글):
  * create_by : foreinKey
  * review : foreinKey
  * body : char
  * create_at : dateTime
  * updated_at : dateTime
* Image(리뷰에서 그림을 여러 장 사용하기 위해 만든 모델)
  * review : foreinKey(Reivew)
  * image : image
* Like(리뷰 좋아요)
  * review : foreinKey(Review)
  * create : foreinKey(User)
  * create_at : dateTime

## Users
커스텀 **유저를** 위한 앱
### Models
* User
  * region : manyToMany(Region)
  * activity : manyToMany(Activity)
  * subject : manyToMany(Subject)
  * profile_image : image

## Services

### Models
* Service
  * title : char = 제목
  * start_data : date = 활동기간 시작 날짜
  * closing_date : date = 활동기간 종료 날자
  * sub_activity : char = 활동분야
  * place : char = 봉사지역
  * sub_subject : char = 봉사장소
  * value : char
  * Region : manyToMany(Region)
  * subject : manyToMany(Subject)
  * activity : manyToMany(Activity)
