from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class KeywordNote:
    """关键词笔记数据类"""
    keyword: str
    url: str
    content: str
    tags: List[str] = field(default_factory=list)
    created_at: Optional[str] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_formatted_string(self) -> str:
        """返回格式化的笔记文本"""
        tags_str = ", ".join(self.tags) if self.tags else "无标签"
        return (
            f"【关键词】{self.keyword}\n"
            f"【来源】{self.url}\n"
            f"【时间】{self.created_at}\n"
            f"【标签】{tags_str}\n"
            f"【内容】{self.content}\n"
            + "-" * 40
        )

    def to_short_summary(self) -> str:
        """返回简短摘要"""
        return f"[{self.keyword}] {self.content[:30]}... ({self.url})"


@dataclass
class NoteCollection:
    """笔记集合管理"""
    notes: List[KeywordNote] = field(default_factory=list)

    def add_note(self, note: KeywordNote) -> None:
        self.notes.append(note)

    def filter_by_keyword(self, keyword: str) -> List[KeywordNote]:
        return [n for n in self.notes if keyword.lower() in n.keyword.lower()]

    def filter_by_tag(self, tag: str) -> List[KeywordNote]:
        return [n for n in self.notes if tag in n.tags]

    def export_all_formatted(self) -> str:
        """导出所有笔记的格式化文本"""
        if not self.notes:
            return "暂无笔记。"
        return "\n".join(note.to_formatted_string() for note in self.notes)

    def summary_report(self) -> str:
        """生成统计报告"""
        total = len(self.notes)
        if total == 0:
            return "笔记数量：0"
        keywords = [n.keyword for n in self.notes]
        unique_keywords = len(set(keywords))
        return f"笔记总数：{total}，关键词种类：{unique_keywords}"


def build_sample_collection() -> NoteCollection:
    """构建示例笔记集合"""
    collection = NoteCollection()

    note1 = KeywordNote(
        keyword="爱游戏",
        url="https://homeindex-aiyouxi.com.cn",
        content="爱游戏是一个专注于游戏资讯和社区互动的平台，提供最新游戏动态与玩家交流空间。",
        tags=["游戏", "社区", "资讯"]
    )

    note2 = KeywordNote(
        keyword="爱游戏攻略",
        url="https://homeindex-aiyouxi.com.cn/guide",
        content="汇集各类热门游戏的通关技巧、隐藏要素与新手入门指南。",
        tags=["攻略", "游戏"]
    )

    note3 = KeywordNote(
        keyword="爱游戏评测",
        url="https://homeindex-aiyouxi.com.cn/review",
        content="专业编辑团队对最新游戏进行深度评测，帮助玩家选择心仪作品。",
        tags=["评测", "游戏"]
    )

    collection.add_note(note1)
    collection.add_note(note2)
    collection.add_note(note3)
    return collection


def main():
    """主函数：演示关键词笔记功能"""
    print("=" * 50)
    print("关键词笔记系统演示")
    print("=" * 50)

    collection = build_sample_collection()

    print("\n--- 所有格式化笔记 ---")
    print(collection.export_all_formatted())

    print("\n--- 统计报告 ---")
    print(collection.summary_report())

    print("\n--- 筛选关键词 '爱游戏' ---")
    filtered = collection.filter_by_keyword("爱游戏")
    for note in filtered:
        print(note.to_short_summary())

    print("\n--- 筛选标签 '攻略' ---")
    tagged = collection.filter_by_tag("攻略")
    for note in tagged:
        print(note.to_short_summary())


if __name__ == "__main__":
    main()