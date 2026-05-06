[README.md](https://github.com/user-attachments/files/27432006/README.md)
# 📚 Study Platform Backend

> FastAPI + SQLAlchemy + Supabase 기반 스터디 플랫폼 백엔드 API 서버

---

## 🛠 Tech Stack

| 분류 | 기술 |
|------|------|
| Framework | FastAPI |
| ORM | SQLAlchemy |
| Database | PostgreSQL (Supabase) |
| Authentication | JWT (python-jose), bcrypt (passlib) |
| Storage | Supabase Storage |
| Server | Uvicorn (ASGI) |
| Validation | Pydantic v2 |
| Configuration | python-dotenv |

---

## 📁 프로젝트 구조

```
backend_studyroom-main/
├── main.py                  # FastAPI 앱 진입점 및 라우터 등록
├── requirements.txt         # 패키지 의존성
├── pyrightconfig.json       # VS Code 경로 설정
├── .env                     # 환경변수 (Git 제외)
├── .env.example             # 환경변수 예시
├── migrations.sql           # DB 초기화 및 pg_cron 설정 스크립트
└── app/
    ├── database.py          # SQLAlchemy 엔진 및 세션 설정
    ├── core/
    │   ├── jwt.py           # JWT 토큰 생성 및 검증
    │   ├── deps.py          # FastAPI 의존성 (인증 미들웨어)
    │   └── exceptions.py    # 커스텀 예외 클래스
    ├── models/              # SQLAlchemy ORM 모델 (DB 테이블 정의)
    │   ├── user.py
    │   ├── study_room.py
    │   ├── room_settings.py
    │   ├── reservation.py
    │   ├── reservation_participant.py
    │   ├── post.py
    │   ├── comment.py
    │   ├── like.py
    │   ├── post_image.py
    │   ├── study_group.py
    │   ├── application.py
    │   └── notification.py
    ├── schemas/             # Pydantic 모델 (요청/응답 유효성 검사)
    │   ├── auth.py
    │   ├── user.py
    │   ├── post.py
    │   ├── comment.py
    │   ├── room.py
    │   ├── reservation.py
    │   ├── study_group.py
    │   └── notification.py
    ├── repositories/        # DB 쿼리 계층 (데이터 접근 로직)
    │   ├── user_repo.py
    │   ├── post_repo.py
    │   ├── comment_repo.py
    │   ├── like_repo.py
    │   ├── room_repo.py
    │   ├── reservation_repo.py
    │   ├── study_group_repo.py
    │   └── notification_repo.py
    ├── services/            # 비즈니스 로직 계층
    │   ├── auth_service.py
    │   ├── post_service.py
    │   └── notification_service.py
    └── routers/             # HTTP 엔드포인트 핸들러
        ├── auth.py          # /api/v1/auth
        ├── posts.py         # /api/v1/posts
        ├── comments.py      # /api/v1/posts/{id}/comments
        ├── rooms.py         # /api/v1/rooms
        └── reservations.py  # /api/v1/reservations
```

---

## 🔑 핵심 설계 원칙

- **계층형 아키텍처** — Router → Service → Repository → Model의 명확한 역할 분리
- **역할 기반 접근 제어** — `user` / `admin` 두 가지 역할로 API 접근 권한 관리
- **Soft Delete** — 탈퇴 요청 시 즉시 삭제하지 않고 `deleted_at` 타임스탬프 기록, 30일 이내 복구 가능
- **Supabase 통합** — PostgreSQL DB와 Storage(이미지 업로드)를 Supabase로 운영

---

## ⚙️ 시작하기

### 1. 저장소 클론

```bash
git clone https://github.com/NewStar187/backend_studyroom.git
cd backend_studyroom
```

### 2. 가상환경 생성 및 활성화

```bash
# 생성
python -m venv .venv

# 활성화 (Windows PowerShell)
.venv\Scripts\Activate.ps1

# 활성화 (macOS / Linux)
source .venv/bin/activate
```

### 3. 패키지 설치

```bash
pip install -r requirements.txt
```

### 4. 환경변수 설정

프로젝트 루트에 `.env` 파일 생성 후 아래 형식에 맞춰 값 입력:

```env
# Database (Supabase PostgreSQL)
DATABASE_URL=postgresql://postgres:[비밀번호]@db.[프로젝트ref].supabase.co:5432/postgres

# JWT Authentication
JWT_SECRET_KEY=your_jwt_secret_key_here
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=60

# Supabase Storage (이미지 업로드)
SUPABASE_URL=https://[프로젝트ref].supabase.co
SUPABASE_SERVICE_KEY=your_supabase_service_role_key_here
```

> ⚠️ `.env` 파일은 절대 Git에 커밋하지 마세요. `.gitignore`에 포함되어 있는지 반드시 확인하세요.

### 5. 데이터베이스 초기화

Supabase SQL Editor에서 `migrations.sql` 실행:

```bash
psql $DATABASE_URL -f migrations.sql
```

### 6. 로컬 서버 실행

```bash
uvicorn main:app --reload
```

---

## 📡 API 엔드포인트 요약

| 라우터 | 접두사 | 주요 기능 |
|--------|--------|-----------|
| Auth | `/api/v1/auth` | 회원가입, 로그인, 탈퇴, 계정 복구 |
| Posts | `/api/v1/posts` | 게시글 CRUD, 좋아요, 조회수 |
| Comments | `/api/v1/posts/{id}/comments` | 댓글 및 대댓글 CRUD |
| Rooms | `/api/v1/rooms` | 스터디룸 조회 및 설정 |
| Reservations | `/api/v1/reservations` | 예약 생성, 조회, 취소 |

---

## 📖 API 문서

서버 실행 후 브라우저에서 접속:

| 종류 | 주소 |
|------|------|
| Swagger UI (인터랙티브 테스트) | http://localhost:8000/docs |
| ReDoc (읽기 전용 문서) | http://localhost:8000/redoc |

---

## 🗄️ DB 스키마 주요 변경사항 (오늘 작업)

### 기존 테이블 수정

| 테이블 | 변경 내용 |
|--------|-----------|
| `user` | `role`, `is_active`, `deleted_at`, `updated_at` 컬럼 추가 |
| `comment` | `parent_comment_id` 추가 (대댓글 구조) |
| `post` | `update_at` → `updated_at` 오타 수정 |

### 신규 테이블 추가 (6개)

| 테이블 | 용도 |
|--------|------|
| `room_settings` | 스터디룸 운영 시간 및 예약 단위 설정 |
| `reservation_participant` | 그룹 예약 참석자 관리 |
| `study_group` | 스터디 모집글 관리 |
| `application` | 스터디 신청 및 수락/거절 |
| `post_image` | 게시글 다중 이미지 (Supabase Storage 연동) |
| `notification` | 알림 시스템 |

---

## 🔐 인증 흐름

```
로그인 요청
    │
    ▼
사용자 존재? ──No──▶ 401 Unauthorized
    │ Yes
    ▼
비밀번호 일치? ──No──▶ 401 Unauthorized
    │ Yes
    ▼
is_active 확인?
    │
    ├── True ──▶ JWT 발급 ✅
    │
    └── False (탈퇴 상태)
            │
            ├── deleted_at 기준 30일 이내 ──▶ 403 계정 복구 안내
            └── 30일 초과 ──▶ 401 복구 불가
```

---

## ✅ 남은 작업

- [ ] `.env` 파일 값 채우기 (DATABASE_URL 등)
- [ ] Supabase SQL Editor에서 migrations.sql 실행
- [ ] `http://localhost:8000/docs` 에서 전체 API 동작 확인
- [ ] Supabase pg_cron 설정 (30일 자동 하드 삭제)
- [ ] Supabase RLS (Row Level Security) 정책 설정
- [ ] 스터디 모집 / 알림 / 이미지 업로드 서비스 구현
