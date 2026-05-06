완료된 작업
1. 프로젝트 구조 분석

기존 코드(models, repositories, routers) 분석
목표 프로젝트 README 분석 (GitHub)
Supabase 스키마 현황 파악
부족한 부분 도출

app/
├── core/
│   ├── __init__.py
│   ├── jwt.py          ✅ 완성
│   ├── exception.py    ✅ 완성
│   └── deps.py         ✅ 완성
├── models/
│   ├── user.py         ✅ 수정 (Boolean, is_active, deleted_at, updated_at 추가)
│   ├── comment.py      ✅ 수정 (parent_comment_id 추가, updated_at 오타 수정)
│   ├── post.py         ✅ 수정 (updated_at 오타 확인)
│   ├── room_settings.py        ✅ 신규 생성
│   ├── reservation_participant.py  ✅ 신규 생성
│   ├── study_group.py          ✅ 신규 생성
│   ├── application.py          ✅ 신규 생성
│   ├── post_image.py           ✅ 신규 생성
│   └── notification.py         ✅ 신규 생성
├── schemas/
│   ├── auth.py         ✅ 완성
│   ├── user.py         ✅ 완성
│   ├── post.py         ✅ 완성
│   ├── comment.py      ✅ 완성
│   ├── room.py         ✅ 완성
│   ├── reservation.py  ✅ 완성
│   ├── study_group.py  ✅ 완성
│   └── notification.py ✅ 완성
├── repositories/
│   ├── user_repo.py        ✅ 완성
│   ├── post_repo.py        ✅ 완성
│   ├── comment_repo.py     ✅ 완성
│   ├── like_repo.py        ✅ 완성
│   ├── room_repo.py        ✅ 완성
│   ├── reservation_repo.py ✅ 완성
│   ├── study_group_repo.py ✅ 완성
│   └── notification_repo.py ✅ 완성
├── services/
│   ├── auth_service.py         ✅ 완성
│   ├── post_service.py         ✅ 완성
│   └── notification_service.py ✅ 완성
├── routers/
│   ├── auth.py         ✅ 완성
│   ├── posts.py        ✅ 완성
│   ├── comments.py     ✅ 완성
│   ├── rooms.py        ✅ 완성
│   └── reservations.py ✅ 완성
├── __init__.py         ✅ 생성
└── database.py         ✅ 완성
pyrightconfig.json      ✅ 생성 (경로 설정)
main.py                 ✅ 완성 (CORS 포함)
