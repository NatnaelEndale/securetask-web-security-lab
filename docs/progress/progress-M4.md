## M4 — PostgreSQL Database Integration

### M4.1 — PostgreSQL Setup
- [x] Installed and configured PostgreSQL 18.
- [x] Created the `securetask_user` database role.
- [x] Created the `securetask_db` development database.
- [x] Created the `securetask_test_db` test database.
- [x] Configured password-based database authentication.
- [x] Verified database connectivity using psql.

### M4.2 — SQLAlchemy Integration
- [x] Installed SQLAlchemy.
- [x] Installed Psycopg 3 PostgreSQL driver.
- [x] Installed and configured Alembic.
- [x] Added environment-based database configuration.
- [x] Created the SQLAlchemy database engine.
- [x] Configured the SQLAlchemy session factory.
- [x] Added `.env` to `.gitignore`.
- [x] Created `.env.example` without real credentials.
- [x] Verified Python-to-PostgreSQL connectivity.

### M4.3 — Database ORM Model
- [x] Created the SQLAlchemy declarative Base.
- [x] Implemented the TaskORM model.
- [x] Defined the tasks table and its columns.
- [x] Configured primary key and database constraints.
- [x] Configured server-side defaults and timestamps.
- [x] Kept the TaskRecord domain model separate from TaskORM.

### M4.4 — Database Migrations
- [x] Initialized Alembic.
- [x] Configured Alembic to use application database metadata.
- [x] Generated the initial tasks table migration.
- [x] Applied the migration to the development database.
- [x] Applied the migration to the test database.
- [x] Verified the migration revision.
- [x] Ran `alembic check` successfully.

### M4.5 — Repository Refactoring
- [x] Replaced the in-memory TaskRepository with a SQLAlchemy-backed repository.
- [x] Implemented task creation.
- [x] Implemented task retrieval.
- [x] Implemented task updates.
- [x] Implemented task deletion.
- [x] Implemented conversion between TaskORM and TaskRecord.
- [x] Kept database operations inside the repository layer.
- [x] Kept transaction management outside the repository.

### M4.6 — FastAPI Database Integration
- [x] Implemented request-scoped database sessions.
- [x] Implemented database commit and rollback handling.
- [x] Connected TaskRepository to the database session.
- [x] Connected TaskService through FastAPI dependencies.
- [x] Removed the global in-memory repository and service instances.
- [x] Preserved the existing API endpoint architecture.

### M4.7 — PostgreSQL Testing and Verification
- [x] Configured a dedicated PostgreSQL test database.
- [x] Implemented isolated database transaction fixtures.
- [x] Configured FastAPI dependency overrides for API tests.
- [x] Updated tests to account for PostgreSQL sequence behavior.
- [x] Verified repository tests.
- [x] Verified service tests.
- [x] Verified API integration tests.
- [x] Verified test database rollback and isolation.
- [x] Verified task creation through the running FastAPI application.
- [x] Verified task retrieval through the API.
- [x] Verified task records directly in PostgreSQL.
- [x] Verified persistence after application restart.

**Verification:** 25 tests passed, 0 failures, 1 deprecation warning.

### M4 Architecture
- [x] Implemented API, service, and repository layers.
- [x] Separated business logic from database access.
- [x] Separated the domain TaskRecord model from the SQLAlchemy ORM model.
- [x] Separated development and test databases.
- [x] Configured PostgreSQL as the persistent data store.

**Architecture:** FastAPI Routes -> Task Service -> Task Repository -> SQLAlchemy -> PostgreSQL.

**Note:** Database access is logically separated through the repository layer. Physical deployment isolation of PostgreSQL from the backend is outside the scope of this milestone.
