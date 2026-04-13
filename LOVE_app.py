# 安装依赖：pip install streamlit
import streamlit as st

# --------------------------
# 1. 页面配置与样式
# --------------------------
st.set_page_config(
    page_title="恋爱人格测试 | 维度加权版",
    page_icon="💘",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 自定义CSS样式
st.markdown("""
<style>
    .stApp {
        max-width: 800px;
        margin: 0 auto;
    }
    .question-card {
        background: linear-gradient(135deg, #fff5f5 0%, #fff0f0 100%);
        padding: 1.2rem;
        border-radius: 20px;
        margin-bottom: 1.2rem;
        border-left: 6px solid #ff6b6b;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
    }
    .question-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(255,107,107,0.15);
    }
    .result-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 24px;
        color: white;
        text-align: center;
        margin: 1rem 0;
    }
    .dimension-bar {
        background-color: rgba(255,255,255,0.2);
        border-radius: 10px;
        height: 8px;
        margin: 5px 0;
    }
    .dimension-fill {
        background-color: #ffd93d;
        border-radius: 10px;
        height: 8px;
        transition: width 0.5s ease;
    }
    .stButton > button {
        background: linear-gradient(135deg, #ff6b6b 0%, #ff8e53 100%);
        color: white;
        font-size: 1.2rem;
        padding: 0.6rem 2rem;
        border-radius: 40px;
        border: none;
        width: 100%;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 20px rgba(255,107,107,0.4);
        color: white;
    }
    footer {
        text-align: center;
        font-size: 0.8rem;
        color: #aaa;
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------
# 2. 题目数据（35题 × 4选项）
# --------------------------
QUESTIONS = [
    "💘 面对喜欢的人，你更倾向于？",
    "💼 恋爱和学业/工作冲突时，你会？",
    "🔥 吵架时你的第一反应是？",
    "🎪 你对恋爱新鲜感的看法是？",
    "👑 择偶最看重对方的？",
    "💌 有人猛烈追求你，你会？",
    "🤝 你认为好的恋爱应该是？",
    "📅 约会行程谁来安排？",
    "📱 朋友约你，你正在和对象聊天，你会？",
    "🎂 对象忘记纪念日/生日，你会？",
    "🫂 你的粘人程度是？",
    "😢 压力大时你需要伴侣？",
    "💰 你的恋爱消费观是？",
    "👀 能接受对象和异性正常互动吗？",
    "🍜 吵架后谁先低头？",
    "📸 对朋友圈秀恩爱的态度？",
    "🎭 你在恋爱里更像？",
    "💔 对方提分手，你的反应是？",
    "❄️ 被对象冷落忽冷忽热，你会？",
    "🎪 恋爱中你更像？",
    "👻 看到对象和前任联系，你会？",
    "💕 你对暧昧的看法是？",
    "✨ 出现新的心动对象，你会？",
    "⚠️ 更讨厌伴侣哪种行为？",
    "🔒 安全感主要来自？",
    "💬 你擅长怎么表达爱意？",
    "🌊 你的情绪风格更像？",
    "🍂 恋爱变平淡，你会？",
    "🎣 单身时有人追但没感觉，你会？",
    "💫 恋爱中遇到更心动的人，你会？",
    "🏝️ 更向往哪种恋爱氛围？",
    "🎁 你更愿意为恋爱付出？",
    "🔧 受不了对象缺点时，你会？",
    "⚡ 感情里你更偏向？",
    "🎯 最后直觉选一个更像你的词："
]

OPTIONS = [
    # 1
    ["🎯 A：疯狂主动，直球出击", "👀 B：慢慢试探，暗中观察", "😎 C：故意冷淡，欲擒故纵", "😴 D：完全无所谓，爱咋咋地"],
    # 2
    ["❤️ A：恋爱至上，工作靠边站", "⚖️ B：尽量平衡，两边都顾", "💰 C：搞钱第一，恋爱随缘", "😪 D：全都摆烂，我先快乐"],
    # 3
    ["😤 A：当场破防，情绪拉满", "🧠 B：冷静讲道理，就事论事", "❄️ C：直接冷战，一句话不说", "🙈 D：懒得吵，直接无视"],
    # 4
    ["🎢 A：必须天天新鲜，不然没意思", "🎁 B：偶尔来点仪式感就够", "🍵 C：平淡最好，别折腾我", "🚪 D：没新鲜感就想换人"],
    # 5
    ["💎 A：颜值氛围，看着舒服", "🤝 B：人品靠谱，性格合得来", "📈 C：条件好，能带我进步", "💝 D：只要对我足够好就行"],
    # 6
    ["🥰 A：立马答应，快乐恋爱", "🔍 B：先了解看看，不着急", "🙅 C：礼貌拒绝，不耽误人", "🎣 D：吊着享受，不主动不负责"],
    # 7
    ["🫂 A：连体婴，时刻黏在一起", "🌳 B：亲密又独立，有各自空间", "🏃 C：各玩各的，互不干涉", "🦅 D：别管我，我要绝对自由"],
    # 8
    ["👑 A：我全包，听我的安排", "🤝 B：一起商量，共同决定", "😴 C：对方安排，我跟着走", "🍿 D：随便都行，别麻烦我"],
    # 9
    ["💕 A：先陪对象，朋友下次", "👫 B：带上对象一起赴约", "📱 C：正常见朋友，对象等等", "🚫 D：直接推掉朋友约会"],
    # 10
    ["😭 A：暴哭伤心，觉得不爱了", "😤 B：有点失落，提醒一下", "📝 C：默默记仇，以后报复", "🤷 D：无所谓，我也记不住"],
    # 11
    ["🦥 A：巨黏人，时刻要报备", "🐱 B：正常黏，适度依赖", "🏠 C：不太黏，需要个人空间", "🦅 D：完全不黏，别来烦我"],
    # 12
    ["🤗 A：抱抱哄我，听我吐槽", "🤫 B：安静陪着，不用多说", "🧘 C：让我自己冷静一会儿", "🔧 D：直接帮我解决问题"],
    # 13
    ["💸 A：舍得花，仪式感拉满", "📊 B：该花就花，理性消费", "🐶 C：能省则省，绝不乱花", "🪙 D：花对方钱，自己一毛不拔"],
    # 14
    ["🚫 A：绝对不行，必须断联", "📏 B：可以，但要保持距离", "🤝 C：无所谓，我也有异性朋友", "🎉 D：支持，多交点更热闹"],
    # 15
    ["😢 A：我先低头，舍不得对方", "⚖️ B：谁错谁低头，讲道理", "😤 C：绝不低头，等对方来哄", "💀 D：直接分手，不废话"],
    # 16
    ["📱 A：天天秀，恨不得全世界知道", "📅 B：纪念日偶尔发一下", "🏠 C：基本不发，低调过日子", "👻 D：坚决不发，怕被围观"],
    # 17
    ["🧠 A：纯纯恋爱脑，情绪被拿捏", "🦸 B：清醒独立，不恋爱脑", "😴 C：摆烂佛系，爱怎样怎样", "👑 D：强势掌控，我说了算"],
    # 18
    ["🙏 A：疯狂挽回，卑微求复合", "🚶 B：尊重选择，体面离开", "❄️ C：冷漠同意，绝不挽留", "💪 D：我先甩，绝不丢面子"],
    # 19
    ["😰 A：胡思乱想，情绪崩溃", "💬 B：直接问清楚，不内耗", "🥶 C：我也冷，看谁熬得过谁", "🎮 D：无所谓，我自己玩更爽"],
    # 20
    ["👨‍👩‍👧 A：大家长，管吃管喝管睡觉", "🤝 B：互相照顾，平等相处", "🧸 C：小朋友，享受被照顾", "🏃 D：各顾各的，别麻烦彼此"],
    # 21
    ["💢 A：当场炸毛，必须吵架", "💬 B：心里不舒服，好好沟通", "📝 C：默默记仇，长期冷战", "😶 D：无所谓，过去就过去了"],
    # 22
    ["🎭 A：超爱暧昧，推拉超快乐", "⚠️ B：适度暧昧，不越界", "⏰ C：不喜欢，浪费时间", "🤢 D：恶心养鱼，坚决拒绝"],
    # 23
    ["🏃 A：立马变心，追新人", "😔 B：有点心动，但会克制", "💪 C：毫无感觉，非常专一", "🎣 D：同时聊，谁好跟谁"],
    # 24
    ["🎲 A：忽冷忽热，总让我猜", "🫂 B：太黏人，没有私人空间", "❄️ C：太冷淡，完全不在乎", "👑 D：太强势，什么都要管"],
    # 25
    ["📱 A：秒回消息，时刻找我", "🔒 B：专一忠诚，边界清晰", "📈 C：物质稳定，有未来规划", "🕊️ D：不管我，给足自由"],
    # 26
    ["💬 A：甜言蜜语，天天说爱", "🎁 B：实际行动，默默付出", "💎 C：送礼物砸钱表达心意", "⏰ D：随叫随到，长期陪伴"],
    # 27
    ["🎢 A：情绪波动大，爱作爱闹", "😊 B：情绪稳定，好沟通", "🧊 C：偏冷漠，不爱表达", "😴 D：佛系摆烂，没啥情绪"],
    # 28
    ["🎆 A：主动制造浪漫，拒绝平淡", "🌊 B：接受平淡，细水长流", "🥀 C：慢慢冷淡，不想继续", "🦋 D：找新欢，寻找刺激"],
    # 29
    ["🎣 A：吊着对方，享受被爱", "✋ B：直接拒绝，不耽误人", "🤔 C：勉强试试，万一合适", "💀 D：已读不回，冷处理"],
    # 30
    ["💔 A：直接出轨，追求新人", "😇 B：克制自己，忠于现任", "💪 C：不会心动，非常专一", "📊 D：对比一下，选更好的"],
    # 31
    ["🔥 A：轰轰烈烈，甜到上头", "🍵 B：安稳舒服，平平淡淡", "🦅 C：轻松自由，互不束缚", "😴 D：躺平享受，不用付出"],
    # 32
    ["⏰ A：全部时间和心思", "💎 B：时间+金钱+真心", "💰 C：只花钱，不想费心", "😴 D：啥都不想付出"],
    # 33
    ["🔧 A：强行改造，改不好就分", "🤝 B：包容理解，慢慢磨合", "😶 C：心里嫌弃，表面忍着", "🏃 D：直接分手，下一个更乖"],
    # 34
    ["⚡ A：主动直球，大胆出击", "😴 B：被动等待，从不主动", "🎭 C：欲擒故纵，玩点套路", "🍃 D：随缘佛系，爱来不来"],
    # 35
    ["🦥 A：粘人 / 深情 / 恋爱脑", "🦸 B：清醒 / 独立 / 理智", "😴 C：佛系 / 摆烂 / 无所谓", "💰 D：高冷 / 搞钱 / 自由"]
]

# --------------------------
# 3. 维度加权映射（每题每个选项的维度分值 1-10分）
# 维度说明：
# D1 - 依赖度：喜欢黏人 vs 独立自由（分越高越黏人）
# D2 - 浪漫值：追求仪式感 vs 务实平淡（分越高越浪漫）
# D3 - 掌控欲：主动掌控 vs 被动随缘（分越高越主动）
# D4 - 忠诚度：专一深情 vs 随性开放（分越高越专一）
# --------------------------
DIMENSION_MAPPING = [
    # 1. 面对喜欢的人
    {"A": {"D1": 8, "D2": 7, "D3": 9, "D4": 7},
     "B": {"D1": 5, "D2": 5, "D3": 4, "D4": 6},
     "C": {"D1": 3, "D2": 6, "D3": 7, "D4": 4},
     "D": {"D1": 1, "D2": 2, "D3": 2, "D4": 3}},
    # 2. 恋爱 vs 工作
    {"A": {"D1": 9, "D2": 7, "D3": 5, "D4": 8},
     "B": {"D1": 6, "D2": 6, "D3": 6, "D4": 7},
     "C": {"D1": 2, "D2": 3, "D3": 8, "D4": 5},
     "D": {"D1": 1, "D2": 1, "D3": 2, "D4": 2}},
    # 3. 吵架反应
    {"A": {"D1": 8, "D2": 4, "D3": 7, "D4": 6},
     "B": {"D1": 5, "D2": 6, "D3": 5, "D4": 7},
     "C": {"D1": 2, "D2": 2, "D3": 8, "D4": 3},
     "D": {"D1": 1, "D2": 1, "D3": 3, "D4": 2}},
    # 4. 新鲜感态度
    {"A": {"D1": 7, "D2": 9, "D3": 6, "D4": 5},
     "B": {"D1": 6, "D2": 7, "D3": 5, "D4": 7},
     "C": {"D1": 3, "D2": 3, "D3": 4, "D4": 6},
     "D": {"D1": 4, "D2": 8, "D3": 5, "D4": 3}},
    # 5. 择偶看重
    {"A": {"D1": 4, "D2": 8, "D3": 5, "D4": 5},
     "B": {"D1": 6, "D2": 6, "D3": 6, "D4": 9},
     "C": {"D1": 3, "D2": 4, "D3": 7, "D4": 6},
     "D": {"D1": 8, "D2": 7, "D3": 3, "D4": 7}},
    # 6. 被猛烈追求
    {"A": {"D1": 8, "D2": 7, "D3": 4, "D4": 6},
     "B": {"D1": 5, "D2": 5, "D3": 3, "D4": 7},
     "C": {"D1": 3, "D2": 4, "D3": 6, "D4": 8},
     "D": {"D1": 2, "D2": 3, "D3": 7, "D4": 2}},
    # 7. 理想恋爱状态
    {"A": {"D1": 10, "D2": 7, "D3": 6, "D4": 8},
     "B": {"D1": 5, "D2": 6, "D3": 5, "D4": 8},
     "C": {"D1": 2, "D2": 3, "D3": 4, "D4": 4},
     "D": {"D1": 1, "D2": 2, "D3": 8, "D4": 5}},
    # 8. 约会安排
    {"A": {"D1": 7, "D2": 6, "D3": 9, "D4": 6},
     "B": {"D1": 6, "D2": 7, "D3": 5, "D4": 7},
     "C": {"D1": 4, "D2": 4, "D3": 2, "D4": 6},
     "D": {"D1": 2, "D2": 2, "D3": 3, "D4": 4}},
    # 9. 朋友vs对象
    {"A": {"D1": 9, "D2": 6, "D3": 5, "D4": 8},
     "B": {"D1": 7, "D2": 7, "D3": 6, "D4": 7},
     "C": {"D1": 3, "D2": 4, "D3": 4, "D4": 5},
     "D": {"D1": 5, "D2": 3, "D3": 7, "D4": 6}},
    # 10. 忘记纪念日
    {"A": {"D1": 9, "D2": 8, "D3": 6, "D4": 7},
     "B": {"D1": 6, "D2": 6, "D3": 5, "D4": 6},
     "C": {"D1": 5, "D2": 4, "D3": 7, "D4": 4},
     "D": {"D1": 2, "D2": 2, "D3": 3, "D4": 3}},
    # 11. 粘人程度
    {"A": {"D1": 10, "D2": 6, "D3": 7, "D4": 8},
     "B": {"D1": 7, "D2": 6, "D3": 5, "D4": 7},
     "C": {"D1": 3, "D2": 5, "D3": 4, "D4": 6},
     "D": {"D1": 1, "D2": 3, "D3": 5, "D4": 4}},
    # 12. 压力时需要伴侣
    {"A": {"D1": 9, "D2": 7, "D3": 6, "D4": 7},
     "B": {"D1": 6, "D2": 5, "D3": 4, "D4": 6},
     "C": {"D1": 3, "D2": 4, "D3": 5, "D4": 5},
     "D": {"D1": 4, "D2": 5, "D3": 7, "D4": 6}},
    # 13. 消费观
    {"A": {"D1": 6, "D2": 9, "D3": 6, "D4": 6},
     "B": {"D1": 5, "D2": 6, "D3": 5, "D4": 7},
     "C": {"D1": 3, "D2": 3, "D3": 7, "D4": 6},
     "D": {"D1": 4, "D2": 2, "D3": 8, "D4": 3}},
    # 14. 异性互动
    {"A": {"D1": 7, "D2": 4, "D3": 8, "D4": 9},
     "B": {"D1": 5, "D2": 5, "D3": 5, "D4": 7},
     "C": {"D1": 4, "D2": 6, "D3": 3, "D4": 5},
     "D": {"D1": 2, "D2": 7, "D3": 2, "D4": 3}},
    # 15. 吵架后谁低头
    {"A": {"D1": 8, "D2": 6, "D3": 4, "D4": 8},
     "B": {"D1": 5, "D2": 6, "D3": 5, "D4": 7},
     "C": {"D1": 4, "D2": 3, "D3": 8, "D4": 4},
     "D": {"D1": 2, "D2": 2, "D3": 9, "D4": 2}},
    # 16. 秀恩爱态度
    {"A": {"D1": 8, "D2": 9, "D3": 6, "D4": 7},
     "B": {"D1": 6, "D2": 7, "D3": 5, "D4": 6},
     "C": {"D1": 3, "D2": 3, "D3": 4, "D4": 5},
     "D": {"D1": 2, "D2": 2, "D3": 5, "D4": 4}},
    # 17. 恋爱中像什么
    {"A": {"D1": 9, "D2": 7, "D3": 5, "D4": 8},
     "B": {"D1": 5, "D2": 6, "D3": 6, "D4": 7},
     "C": {"D1": 2, "D2": 3, "D3": 3, "D4": 4},
     "D": {"D1": 6, "D2": 5, "D3": 9, "D4": 6}},
    # 18. 对方提分手
    {"A": {"D1": 9, "D2": 6, "D3": 4, "D4": 8},
     "B": {"D1": 5, "D2": 5, "D3": 5, "D4": 7},
     "C": {"D1": 3, "D2": 3, "D3": 7, "D4": 4},
     "D": {"D1": 4, "D2": 4, "D3": 8, "D4": 3}},
    # 19. 被冷落反应
    {"A": {"D1": 9, "D2": 6, "D3": 5, "D4": 7},
     "B": {"D1": 6, "D2": 6, "D3": 6, "D4": 7},
     "C": {"D1": 3, "D2": 3, "D3": 8, "D4": 4},
     "D": {"D1": 2, "D2": 4, "D3": 4, "D4": 5}},
    # 20. 恋爱中角色
    {"A": {"D1": 7, "D2": 5, "D3": 9, "D4": 7},
     "B": {"D1": 5, "D2": 6, "D3": 5, "D4": 7},
     "C": {"D1": 8, "D2": 7, "D3": 3, "D4": 6},
     "D": {"D1": 2, "D2": 4, "D3": 7, "D4": 4}},
    # 21. 看到前任联系
    {"A": {"D1": 8, "D2": 3, "D3": 8, "D4": 9},
     "B": {"D1": 5, "D2": 5, "D3": 5, "D4": 7},
     "C": {"D1": 4, "D2": 4, "D3": 7, "D4": 5},
     "D": {"D1": 2, "D2": 5, "D3": 3, "D4": 4}},
    # 22. 对暧昧看法
    {"A": {"D1": 6, "D2": 8, "D3": 7, "D4": 3},
     "B": {"D1": 5, "D2": 6, "D3": 5, "D4": 6},
     "C": {"D1": 3, "D2": 4, "D3": 4, "D4": 7},
     "D": {"D1": 2, "D2": 2, "D3": 3, "D4": 9}},
    # 23. 出现心动对象
    {"A": {"D1": 5, "D2": 7, "D3": 8, "D4": 2},
     "B": {"D1": 6, "D2": 5, "D3": 4, "D4": 7},
     "C": {"D1": 7, "D2": 6, "D3": 5, "D4": 9},
     "D": {"D1": 4, "D2": 6, "D3": 7, "D4": 3}},
    # 24. 讨厌伴侣行为
    {"A": {"D1": 7, "D2": 5, "D3": 6, "D4": 6},
     "B": {"D1": 8, "D2": 4, "D3": 5, "D4": 5},
     "C": {"D1": 3, "D2": 5, "D3": 4, "D4": 7},
     "D": {"D1": 5, "D2": 6, "D3": 8, "D4": 6}},
    # 25. 安全感来源
    {"A": {"D1": 9, "D2": 6, "D3": 7, "D4": 8},
     "B": {"D1": 7, "D2": 7, "D3": 6, "D4": 9},
     "C": {"D1": 4, "D2": 5, "D3": 8, "D4": 7},
     "D": {"D1": 3, "D2": 4, "D3": 5, "D4": 6}},
    # 26. 表达爱意方式
    {"A": {"D1": 8, "D2": 9, "D3": 6, "D4": 7},
     "B": {"D1": 6, "D2": 7, "D3": 5, "D4": 8},
     "C": {"D1": 5, "D2": 8, "D3": 6, "D4": 6},
     "D": {"D1": 7, "D2": 6, "D3": 5, "D4": 7}},
    # 27. 情绪风格
    {"A": {"D1": 8, "D2": 7, "D3": 6, "D4": 6},
     "B": {"D1": 5, "D2": 6, "D3": 5, "D4": 7},
     "C": {"D1": 3, "D2": 4, "D3": 6, "D4": 6},
     "D": {"D1": 2, "D2": 3, "D3": 4, "D4": 5}},
    # 28. 恋爱变平淡
    {"A": {"D1": 7, "D2": 9, "D3": 8, "D4": 6},
     "B": {"D1": 6, "D2": 6, "D3": 5, "D4": 7},
     "C": {"D1": 4, "D2": 3, "D3": 4, "D4": 5},
     "D": {"D1": 5, "D2": 8, "D3": 7, "D4": 3}},
    # 29. 单身被追没感觉
    {"A": {"D1": 3, "D2": 4, "D3": 6, "D4": 3},
     "B": {"D1": 4, "D2": 5, "D3": 5, "D4": 8},
     "C": {"D1": 6, "D2": 5, "D3": 4, "D4": 6},
     "D": {"D1": 2, "D2": 3, "D3": 7, "D4": 4}},
    # 30. 恋爱遇更心动
    {"A": {"D1": 4, "D2": 6, "D3": 8, "D4": 2},
     "B": {"D1": 6, "D2": 5, "D3": 5, "D4": 8},
     "C": {"D1": 7, "D2": 6, "D3": 5, "D4": 9},
     "D": {"D1": 5, "D2": 6, "D3": 7, "D4": 4}},
    # 31. 向往恋爱氛围
    {"A": {"D1": 8, "D2": 9, "D3": 7, "D4": 7},
     "B": {"D1": 5, "D2": 6, "D3": 5, "D4": 8},
     "C": {"D1": 3, "D2": 5, "D3": 6, "D4": 6},
     "D": {"D1": 2, "D2": 3, "D3": 4, "D4": 5}},
    # 32. 愿意付出什么
    {"A": {"D1": 9, "D2": 7, "D3": 6, "D4": 8},
     "B": {"D1": 7, "D2": 8, "D3": 7, "D4": 8},
     "C": {"D1": 4, "D2": 6, "D3": 5, "D4": 5},
     "D": {"D1": 2, "D2": 2, "D3": 3, "D4": 3}},
    # 33. 受不了缺点
    {"A": {"D1": 5, "D2": 4, "D3": 8, "D4": 5},
     "B": {"D1": 6, "D2": 6, "D3": 5, "D4": 8},
     "C": {"D1": 4, "D2": 4, "D3": 4, "D4": 5},
     "D": {"D1": 3, "D2": 5, "D3": 7, "D4": 4}},
    # 34. 感情里偏向
    {"A": {"D1": 7, "D2": 6, "D3": 9, "D4": 7},
     "B": {"D1": 4, "D2": 5, "D3": 3, "D4": 6},
     "C": {"D1": 5, "D2": 6, "D3": 6, "D4": 5},
     "D": {"D1": 3, "D2": 4, "D3": 5, "D4": 6}},
    # 35. 更像的词
    {"A": {"D1": 9, "D2": 8, "D3": 6, "D4": 8},
     "B": {"D1": 4, "D2": 6, "D3": 7, "D4": 7},
     "C": {"D1": 2, "D2": 3, "D3": 4, "D4": 5},
     "D": {"D1": 3, "D2": 5, "D3": 8, "D4": 6}}
]

# --------------------------
# 4. 人格类型库（12种）
# --------------------------
PERSONALITY_TYPES = {
    1: {"name": "黏人粘墙型", "emoji": "🦥",
        "desc": "走哪跟哪，消息秒回，离开三分钟就开始想念，人形挂件本人，没对方活不了。",
        "dimensions": {"D1": 9, "D2": 6, "D3": 5, "D4": 8}},
    2: {"name": "恋爱脑上头型", "emoji": "🧠",
        "desc": "对象放个屁都觉得香，朋友劝不动，道理听不进，为爱降智第一名。",
        "dimensions": {"D1": 8, "D2": 7, "D3": 4, "D4": 7}},
    3: {"name": "嘴硬心软型", "emoji": "😤",
        "desc": "吵架嘴比石头硬，哄人脸比棉花软，嘴上全是嫌弃，心里全是在意。",
        "dimensions": {"D1": 6, "D2": 5, "D3": 7, "D4": 7}},
    4: {"name": "摆烂躺平型", "emoji": "🛌",
        "desc": "不惊喜不浪漫不仪式感，能活着就行，谈个恋爱跟合租室友似的。",
        "dimensions": {"D1": 2, "D2": 2, "D3": 3, "D4": 4}},
    5: {"name": "精致浪漫型", "emoji": "✨",
        "desc": "过节必发圈，礼物要精致，恋爱谈得像拍MV，现实里矫情得一批。",
        "dimensions": {"D1": 6, "D2": 9, "D3": 6, "D4": 6}},
    6: {"name": "大家长管家型", "emoji": "👨‍👩‍👧",
        "desc": "管吃管喝管花钱，比亲妈还能唠叨，明明谈恋爱，活成对方监护人。",
        "dimensions": {"D1": 7, "D2": 5, "D3": 8, "D4": 7}},
    7: {"name": "单身爽翻型", "emoji": "🎉",
        "desc": "一个人吃喝玩乐自由到飞起，恋爱？别来沾边，影响我潇洒。",
        "dimensions": {"D1": 2, "D2": 4, "D3": 6, "D4": 4}},
    8: {"name": "高冷寡王型", "emoji": "❄️",
        "desc": "对谁都没兴趣，内心毫无波澜，主打一个莫挨老子。",
        "dimensions": {"D1": 2, "D2": 3, "D3": 5, "D4": 5}},
    9: {"name": "卷王搞事业型", "emoji": "📈",
        "desc": "对象只会影响我拔剑的速度，学业/搞钱才是真爱，爱情靠边站。",
        "dimensions": {"D1": 2, "D2": 3, "D3": 8, "D4": 5}},
    10: {"name": "怕麻烦回避型", "emoji": "🏃",
         "desc": "暧昧都嫌累，聊天都费劲，谈个恋爱还要磨合？直接劝退。",
         "dimensions": {"D1": 3, "D2": 3, "D3": 4, "D4": 6}},
    11: {"name": "宁缺毋滥挑剔型", "emoji": "👑",
         "desc": "看谁都差点意思，标准高到上天，宁愿孤寡一生，绝不委屈自己。",
         "dimensions": {"D1": 4, "D2": 5, "D3": 6, "D4": 8}},
    12: {"name": "海王养鱼型", "emoji": "🐟",
         "desc": "不谈恋爱，只搞暧昧，广撒网不收网，享受被追捧但绝不负责。",
         "dimensions": {"D1": 3, "D2": 6, "D3": 7, "D4": 2}}
}


# --------------------------
# --------------------------
# 5. 维度加权计分函数（修复版）
# --------------------------
def extract_option_letter(ans):
    """从选项字符串中提取A/B/C/D字母"""
    if not ans:
        return None
    # 查找 "A：" 或 "B：" 等模式
    for letter in ["A", "B", "C", "D"]:
        if f"{letter}：" in ans:
            return letter
    return None


def calculate_dimensions(answers):
    """计算4个维度的总分"""
    dimensions = {"D1": 0, "D2": 0, "D3": 0, "D4": 0}
    count = 0

    for i, ans in enumerate(answers):
        if ans is None or i >= len(DIMENSION_MAPPING):
            continue
        # 提取选项字母 (A/B/C/D)
        letter = extract_option_letter(ans)
        if letter and letter in DIMENSION_MAPPING[i]:
            dims = DIMENSION_MAPPING[i][letter]
            for d in dimensions:
                dimensions[d] += dims[d]
            count += 1

    # 计算平均分（0-10分）
    if count > 0:
        for d in dimensions:
            dimensions[d] = round(dimensions[d] / count, 1)
    else:
        # 如果没有匹配到任何答案，返回默认值
        dimensions = {"D1": 5, "D2": 5, "D3": 5, "D4": 5}

    return dimensions


def calculate_type_from_dimensions(dimensions):
    """根据维度得分匹配最接近的人格类型"""
    best_type = None
    min_distance = float('inf')

    for type_id, type_info in PERSONALITY_TYPES.items():
        # 计算欧氏距离
        distance = 0
        for d in ["D1", "D2", "D3", "D4"]:
            user_val = dimensions.get(d, 5)
            type_val = type_info["dimensions"].get(d, 5)
            distance += (user_val - type_val) ** 2
        distance = distance ** 0.5

        if distance < min_distance:
            min_distance = distance
            best_type = type_id

    return best_type if best_type else 2  # 默认返回恋爱脑
# --------------------------
# 6. 主界面
# --------------------------
st.title("💘 恋爱人格测试 · 维度加权版")
st.caption("35道题，基于4大维度科学分析你的恋爱人格")

with st.expander("📖 测试说明"):
    st.markdown("""
    - 共 **35题**，每题4个选项
    - 测试基于4个核心维度：**依赖度、浪漫值、掌控欲、忠诚度**
    - 请凭第一直觉作答，不要犹豫
    - 结果会生成你的专属恋爱人格和搞笑吐槽
    - 测试结果仅供娱乐，开心最重要～
    """)

    st.markdown("""
    **🎯 四个维度解释：**
    - 💕 **依赖度**：越高越黏人，越低越独立
    - ✨ **浪漫值**：越高越注重仪式感，越低越务实
    - 👑 **掌控欲**：越高越主动掌控，越低越被动随缘
    - 🔒 **忠诚度**：越高越专一深情，越低越随性开放
    """)

# 初始化 session_state
if 'answers' not in st.session_state:
    st.session_state.answers = [None] * len(QUESTIONS)

if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# 显示题目
for i, (question, opts) in enumerate(zip(QUESTIONS, OPTIONS)):
    with st.container():
        st.markdown(f'<div class="question-card">', unsafe_allow_html=True)
        st.markdown(f"**Q{i + 1}.** {question}")

        current_answer = st.session_state.answers[i]
        if current_answer in opts:
            idx = opts.index(current_answer)
        else:
            idx = 0

        answer = st.radio(
            "",
            opts,
            key=f"q_{i}",
            label_visibility="collapsed",
            index=idx
        )
        st.session_state.answers[i] = answer
        st.markdown('</div>', unsafe_allow_html=True)

# 提交按钮
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    submitted = st.button("✨ 生成我的恋爱人格 ✨", use_container_width=True)

# 处理提交
if submitted or st.session_state.submitted:
    if None in st.session_state.answers:
        st.warning("⚠️ 请完成所有题目再提交哦～")
        st.session_state.submitted = False
    else:
        st.session_state.submitted = True

        # 计算维度得分
        dimensions = calculate_dimensions(st.session_state.answers)

        # 计算人格类型
        type_id = calculate_type_from_dimensions(dimensions)
        result = PERSONALITY_TYPES[type_id]


        # 统计选项分布（修复版：用 "A：" 包含判断，而不是 startswith）
        # 统计选项分布（修复版）
        def count_options(answers):
            a = b = c = d = 0
            for ans in answers:
                if ans:
                    if "A：" in ans:
                        a += 1
                    elif "B：" in ans:
                        b += 1
                    elif "C：" in ans:
                        c += 1
                    elif "D：" in ans:
                        d += 1
            return a, b, c, d


        a_count, b_count, c_count, d_count = count_options(st.session_state.answers)

        # 显示结果
        st.balloons()

        # 维度可视化
        st.markdown(f"""
        <div class="result-card">
            <h2>{result['emoji']} {result['name']} {result['emoji']}</h2>
            <p style="font-size: 1.1rem; margin-top: 0.5rem;">💥 {result['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

        # 显示4维度得分条
        st.markdown("### 📊 你的恋爱维度分析")

        dim_names = {"D1": "💕 依赖度", "D2": "✨ 浪漫值", "D3": "👑 掌控欲", "D4": "🔒 忠诚度"}
        dim_colors = {"D1": "#ff6b6b", "D2": "#ffb347", "D3": "#4ecdc4", "D4": "#95e77e"}

        for d, name in dim_names.items():
            score = dimensions.get(d, 5)
            st.markdown(f"""
            <div style="margin-bottom: 15px;">
                <div style="display: flex; justify-content: space-between;">
                    <span>{name}</span>
                    <span><strong>{score}/10</strong></span>
                </div>
                <div class="dimension-bar">
                    <div class="dimension-fill" style="width: {score * 10}%; background-color: {dim_colors[d]}"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # 显示选项统计
        st.markdown(f"""
        <div style="background: #f0f0f0; padding: 1rem; border-radius: 16px; margin-top: 1rem;">
            <p style="text-align: center; margin: 0;">
                🅰️ {a_count}个 &nbsp;&nbsp;|&nbsp;&nbsp;
                🅱️ {b_count}个 &nbsp;&nbsp;|&nbsp;&nbsp;
                ©️ {c_count}个 &nbsp;&nbsp;|&nbsp;&nbsp;
                🅳️ {d_count}个
            </p>
        </div>
        """, unsafe_allow_html=True)

        # 添加趣味分享文案
        st.info(
            f"📢 分享你的结果：我刚测出我是【{result['name']}】{result['emoji']}！依赖度{dimensions['D1']} 浪漫值{dimensions['D2']} 掌控欲{dimensions['D3']} 忠诚度{dimensions['D4']}～快来测测你是哪种恋爱人格！")

        # 重测按钮
        col_reset1, col_reset2, col_reset3 = st.columns([1, 2, 1])
        with col_reset2:
            if st.button("🔄 重新测试", use_container_width=True):
                st.session_state.answers = [None] * len(QUESTIONS)
                st.session_state.submitted = False
                st.rerun()

# 页脚
st.markdown("---")
st.caption("⚡ 测试结果仅供参考 | 基于4维度加权算法 | 开心最重要")