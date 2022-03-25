_斜體部分_ 可刪。

# Ready for Review Check List
- [ ] 已理解最新版的 [Code Review Guideline for aetherAI](https://gitlab.com/DYSK_Labs/the-hitchhiker-s-guide-to-the-web-team/-/wikis/Code-Review-Guideline-for-aetherAI)。
- [ ] 聲明目的、可能影響，確認改動與之符合。
- [ ] 提供充分資訊，包括 易讀的程式 / comments / 其他背景資訊 以利 Review 進行。
- [ ] 提供充分 Keywords 和 Labels，以利未來搜尋。
- [ ] 根據 [Verification Policy](https://gitlab.com/DYSK_Labs/the-hitchhiker-s-guide-to-the-web-team/-/wikis/Merge-Request-Verification-Policy)，驗證改動可行。
  - [ ] Unittest
  - [ ] End to end
     - [ ] _Designer who_
- [ ] 若有任何參與協助者，提及他們的貢獻並表達感謝。
- [ ] 若引用外部資源（如 stack overflow 或開源套件），附上來源並明白相關之 LICENSE 和 copyright 內容。[懶人包](https://gitlab.com/DYSK_Labs/the-hitchhiker-s-guide-to-the-web-team/-/wikis/Software-LICENSE-%E6%87%B6%E4%BA%BA%E5%8C%85)

# 目的

_描述此 MR 為何需要被 merge，如 feature 實作 / 修 bug / 效能改善 / 設計改善。_

# Keywords
_方便搜尋用，隨性打，如：改動檔名 / packages。_

# 改動

_條列式說明改動內容和其影響，行為描述先於實作細節。_

_範例：_
- _`function_with_bug` 在 `x` 為正整數時才會正確，故補上 guard clause raise `ValueError` 提醒使用者。_
- _改變了 `test_blabla` parametrize 的方式，讓加 test case 可以寫更少 code。_
- _把 `function_b` 從 `a.py` 移到 `b.py`，因其與 `b` 更加相關。_
- _裝了 `third_party_package ^1.2.3` (MIT LICENSE)_

# Note

_Optional，其他未來回顧時需要的內容，例如當下時空背景的敘述。_

_範例：_
- _目前 `function_hardcode` 只在 ABC 狀況下使用，就不花太多時間支援更多 case 了。_
- _`StrangeInterface` 還在試驗階段，已註記 unstable，待需求更明朗時可重構。_
- _在 KKK 狀況下回 404 是有點奇怪，但還沒找到 best practice。_
- _`function_dirty` 寫得很醜，沒有想法..._

# Future Work

_Optional，在 MR merge 之後會執行的計畫，可以是 Author 自己的規劃或 Reviewer `nit:` 的內容。_

_範例：_
- _同意 Reviewer XX 說的 `function_bruteforce` 的效能問題，有查到 YY 演算法 (link) 適合這個問題，已開 task 追蹤 (link)。_
- _`other_package` 快開發到一段落了，引入之後就可以把 `old_fashion_utils` 刪掉。_
- _測試還沒包含 ZZ 狀況，PM 說這次的 demo case 是可以控制的，在那之後補上。_

# Approval Check List (for Reviewer)
- [ ] 已理解最新版的 [Code Review Guideline for aetherAI](https://gitlab.com/DYSK_Labs/the-hitchhiker-s-guide-to-the-web-team/-/wikis/Code-Review-Guideline-for-aetherAI)，且依此進行 review。
- [ ] Ready for Review Check List 的每一項皆成立。
- [ ] CI 通過。
- [ ] Author **在此 MR** 提供的資訊，足夠使人明白其實作意圖和可能影響。
- [ ] Edge cases / bugs / 風險 已被設想和提出，並同意 Author 的解決方案 / 未解決的理由。
- [ ] Author 已將必要但不緊急的改動建議列在 Future Work。
