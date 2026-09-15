# Assessment Manifest

## Deliverables

- 12 test files covering T01–T12.
- 52 standard Parts/Stages plus adaptive question banks.
- Protocol for sequential delivery and adaptive difficulty.
- Assessor guide with five scoring dimensions, 15 competency weights, hard gates, confidence and role readiness.
- Answer, progress and final-report templates.
- Three executable practical targets for Programming, Debugging and RAG.

## Replaced/removed old test artifacts

- `../01-bai-test-dau-vao.md`
- `../02-rubric-cham-diem.md`
- `../PHIEU_TRA_LOI.md`
- toàn bộ `../test-theo-cap-do/`
- toàn bộ `../diagnostic/`

Các file roadmap, portfolio, nguồn đối chiếu, bài làm trong Downloads và nội dung trong thư mục `../tâm/` không bị xóa.

## Validation

- Python syntax: 6/6 practical source/test files parse thành công.
- T03 public tests: 5 tests collected; baseline dừng ở `NotImplementedError` theo chủ ý.
- T07 public tests: 5 tests collected; baseline có 4 failures + 1 error theo chủ ý để candidate debug.
- T10 public tests: 4 tests collected; baseline dừng ở `NotImplementedError` theo chủ ý.
- Không coi baseline failing tests là implementation failure của bộ đề.
- Overall candidate score/level vẫn `UNKNOWN` cho đến khi assessment có đủ evidence.

## Start point

`tests/01-logic-reasoning.md` → `Part 1`
