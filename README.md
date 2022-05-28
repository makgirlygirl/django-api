# django-api
paragraph, question GET, POST API

## API 명세서

# 1. [GET] /paragraph

: 지문 전체 리스트 가져오기

### *응답 예시

```json
[
   {
      "paragraphId":1,
      "paragraphBody":"adskjfhn,ekwjbflkewbdkdkdk dkajfnweinfakjsd"
   },
   {
      "paragraphId":2,
      "paragraphBody":"lllledowkdjnvnnbnbnbnnnnkdk dkajfnweinfakjsd"
   },
   {
      "paragraphId":3,
      "paragraphBody":"kljnaszkisenrlisekwjbflkewbdkdkdkdkajfnweinfakjsd"
   },
   {
      "paragraphId":4,
      "paragraphBody":"akljnaszkisenrlisekwjbflkewbdkdkdkdkajfnweinfakjsd"
   },
   {
      "paragraphId":3,
      "paragraphBody":"dddddskjfhn,ekwjbflkewbdkdkdk dkajfnweinfakjsd"
   },
   {
      "paragraphId":4,
      "paragraphBody":"kkkkkkkddddskjfhn,ekwjbflkewbdkdkdk dkajfnweinfakjsd"
   }
]
```

# 2. [GET] /paragraph/{id}

: id가 {id}인 지문 정보 가져오기

### *요청 예시

localhost:8000/paragraph/4

### *응답 예시

```json
{
    "paragraphId": 4, 
    "paragraphBody": "kkkkkkkddddskjfhn,ekwjbflkewbdkdkdk dkajfnweinfakjsd"
}
```

# 3. [POST] /new_paragraph

: 새로운 지문 정보 DB로 보내기

### *요청 예시

```json
{
    "paragraphId": 4, 
    "paragraphBody": "kkkkkkkddddskjfhn,ekwjbflkewbdkdkdk dkajfnweinfakjsd"
}
```

### *응답 예시

(요청이 제대로 된 경우, 그대로 정보 출력)

```json
{
    "paragraphId": 4, 
    "paragraphBody": "kkkkkkkddddskjfhn,ekwjbflkewbdkdkdk dkajfnweinfakjsd"
}
```

# 4. [GET] /question

: 질문 전체 리스트 가져오기

### *응답 예시

```json
[
   {
      "questionId":1,
      "paragraph":1,
      "questionTitle":"akljnaszkisenrlisekwjbflkewbdkdkdkdkajfnweinfakjsd",
      "answer":"hihi",
      "distractor1":"adlfkew",
      "distractor2":"dadlfkew",
      "distractor3":"fadlfkew",
      "distractor4":"hhadlfkew"
   },
   {
      "questionId":2,
      "paragraph":2,
      "questionTitle":"dlafknsdlfnewlnfakjsd",
      "answer":"beybeyb",
      "distractor1":"dlaifh",
      "distractor2":"dasdfdadadlfkew",
      "distractor3":"fadalfkew",
      "distractor4":"hhadlfkew"
   },
   {
      "questionId":3,
      "paragraph":2,
      "questionTitle":"dddddddddd",
      "answer":"bbbbbbbb",
      "distractor1":"dddddddlaifh",
      "distractor2":"daaaaaaasdfdadadlfkew",
      "distractor3":"fadalfdkew",
      "distractor4":"hhadlfkew"
   }
]
```

# 5. [GET] /question/{id}

: id가 {id}인 질문 가져오기

### *요청 예시

localhost:8000/question/4

### *응답 예시

```json
{
   "questionId":4,
   "paragraph":2,
   "questionTitle":"dddddddddd",
   "answer":"bbbbbbbb",
   "distractor1":"dddddddlaifh",
   "distractor2":"daaaaaaasdfdadadlfkew",
   "distractor3":"fadalfdkew",
   "distractor4":"hhadlfkew"
}
```

# 6. [POST] /new_question

: 새로운 질문 정보 DB로 보내기

### *요청 예시

```json
{
   "questionId":4,
   "paragraph":2,
   "questionTitle":"dddddddddd",
   "answer":"bbbbbbbb",
   "distractor1":"dddddddlaifh",
   "distractor2":"daaaaaaasdfdadadlfkew",
   "distractor3":"fadalfdkew",
   "distractor4":"hhadlfkew"
}
```

### *응답 예시

(요청이 제대로 된 경우, 그대로 정보 출력)
```json
{
   "questionId":4,
   "paragraph":2,
   "questionTitle":"dddddddddd",
   "answer":"bbbbbbbb",
   "distractor1":"dddddddlaifh",
   "distractor2":"daaaaaaasdfdadadlfkew",
   "distractor3":"fadalfdkew",
   "distractor4":"hhadlfkew"
}
```
