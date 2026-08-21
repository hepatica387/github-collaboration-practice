# GitHub Collaboration Practice

GitHub를 활용한 **2인 협업 연습 프로젝트**입니다.

## 팀원

| 역할 | 이름   |
| ---- | ------ |
| 팀장 | 정석진 |
| 팀원 | 김동규 |

## 연습 목표

- GitHub Repository 생성 및 관리
- Branch 생성 및 작업
- Commit Convention 적용
- Pull Request 생성
- Code Review
- Merge
- Conflict 발생 및 해결
- `main`, `develop`, `feature` 브랜치 전략 연습

## Branch Convention

```text
main
develop
feature/기능명
```

예시:

```text
feature/member-create
feature/member-list
feature/member-update
```

## Commit Convention

| Type       | 설명                       |
| ---------- | -------------------------- |
| `feat`     | 새로운 기능 추가           |
| `fix`      | 버그 수정                  |
| `refactor` | 코드 리팩토링              |
| `docs`     | 문서 작성 및 수정          |
| `test`     | 테스트 코드 작성           |
| `style`    | 코드 스타일 수정           |
| `chore`    | 프로젝트 설정 및 기타 작업 |

### Commit 예시

```text
chore: 프로젝트 초기 설정

feat: 회원 등록 기능 추가

fix: 회원 조회 오류 수정

refactor: 회원 서비스 로직 개선

docs: README 작성
```

## 협업 방식

1. `develop` 브랜치에서 새로운 `feature` 브랜치를 생성합니다.
2. 각자 맡은 기능을 개발합니다.
3. 작업 완료 후 Commit 및 Push합니다.
4. GitHub에서 `develop` 브랜치를 대상으로 Pull Request를 생성합니다.
5. 상대방이 Code Review를 진행합니다.
6. 리뷰가 완료되면 `develop` 브랜치에 Merge합니다.
7. 기능 개발이 완료되면 `develop`을 `main`에 Merge합니다.

## 역할

### 정석진 - 팀장

- Repository 생성 및 초기 설정
- `main`, `develop` 브랜치 관리
- Pull Request 관리
- Code Review
- Merge 관리

### 김동규 - 팀원

- Repository Clone
- Feature Branch 생성
- 기능 개발
- Pull Request 작성
- Code Review 반영
- Conflict 해결 연습

## Git 기본 명령어

```bash
git clone <repository-url>

git branch

git checkout develop

git checkout -b feature/기능명

git add .

git commit -m "feat: 기능 설명"

git push -u origin feature/기능명

git pull origin develop

git merge develop
```

## 프로젝트 목적

실제 개발 협업에서 사용하는 Git/GitHub 흐름을 직접 실습하며
브랜치 관리, Pull Request, Code Review, Merge Conflict 해결 과정을 익히는 것을 목표로 합니다.
