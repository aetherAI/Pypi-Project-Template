# Check List

- [ ] 我和 Reviewer 皆已閱讀最新版的 [Code Review Guideline for aetherAI](https://gitlab.com/DYSK_Labs/the-hitchhiker-s-guide-to-the-web-team/-/wikis/Code-Review-Guideline-for-aetherAI)。
- [ ] 我已清楚聲明此 MR 的目的和可能影響。
- [ ] 我已確認此 MR 的改動與上述目的相符合。
- [ ] 我已提供充分的資訊，包括 可讀的程式 / comments / 其他背景資訊 以利 Review 進行。
- [ ] 我已提供充分的關鍵字和 Labels，讓未來回顧時能找到此 MR。
- [ ] 我已透過自動化測試或 End-to-End 測試 (並附上證據如截圖)，驗證改動可行。
- [ ] 我已充分提及過程中的參與者 / 協助者 / 參考的外部資訊 (如 stack overflow 或開源套件)，並明白相關之 LICENSE 和 copyright 內容。

# 目的

描述此 MR 為何需要被 merge，如 feature 實作 / 修 bug / 效能改善 / 設計改善。

# 改動

條列式說明改動內容和其影響，行為描述先於實作細節。

範例：
- 讓 `function_with_bug` 在 `arg0` 非正整數時 raise `ValueError` 提醒使用者。
- 改變了 `test_blabla` parametrize 的方式，讓加 test case 可以寫更少 code。
- 把 `function_b` 從 `a.py` 移到 `b.py`，因其與 `b` 更加相關。

# Note

其他未來回顧時需要的內容。

# Future Work

Optional，可以是 author 自己的規劃或 reviewer `nit:` 的內容。
