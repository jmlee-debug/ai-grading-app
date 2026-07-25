import streamlit as st
import re

# --- 페이지 설정 ---
st.set_page_config(page_title="서논술형 자동 채점 시스템", layout="wide")
st.title("📝 2회고사 대비 서논술형 자동 채점 시스템")
st.markdown("---")

# --- 채점 로직 함수 ---

def grade_set_1(q1_1, q1_2, q1_3, q2, q3_a, q3_a_eff, q3_b, q3_b_eff):
    results = {}
    
    # [서논술형 1] 채점
    # 1-1: 쉬운/노력 필요 없음 (오개념 방지: '어려운' 포함 시 오답)
    if "어려운" in q1_1:
        res1_1 = "❌ 오답 (오개념: 어려운 과제가 아님)"
    elif any(k in q1_1 for k in ["쉬운", "노력", "친숙"]):
        res1_1 = "✅ 정답"
    else:
        res1_1 = "❌ 오답 (키워드 부족)"

    # 1-2: 혼자/차분하게/집중
    if all(k in q1_2 for k in ["혼자", "집중"]) or "차분" in q1_2:
        res1_2 = "✅ 정답"
    elif "함께" in q1_2 or "모임" in q1_2:
        res1_2 = "❌ 오답 (오개념: 혼자 해야 함)"
    else:
        res1_2 = "❌ 오답 (키워드 부족: '혼자', '집중' 필요)"
        
    # 1-3: 사회적 억제
    if "억제" in q1_3 and "촉진" not in q1_3:
        res1_3 = "✅ 정답"
    else:
        res1_3 = "❌ 오답 (정확한 용어 '사회적 억제' 필요)"
        
    results['Q1'] = f"- (1) {res1_1}\n- (2) {res1_2}\n- (3) {res1_3}"

    # [서논술형 2] 채점
    # 조건: 괄호 안에 설명 방법 명칭 표기, 지문 내용 한정, 논리적 흐름
    methods_used = re.findall(r'\((.*?)\)', q2)
    valid_methods = ["정의", "예시", "인과", "분석", "비교와 대조", "분류와 구분"]
    found_methods = [m for m in methods_used if any(v in m for v in valid_methods)]
    
    if len(set(found_methods)) >= 2:
        # 방법론 특성 확인 로직
        if "비교" in str(found_methods) and not any(k in q2 for k in ["반면", "다르다", "지만", "차이"]):
            results['Q2'] = "⚠️ 부분 점수: '비교와 대조'를 선택했으나 대조를 나타내는 서술어(반면, ~지만 등)가 부족합니다."
        elif "예시" in str(found_methods) and not any(k in q2 for k in ["예를 들어", "예컨대", "커피숍", "도서관"]):
            results['Q2'] = "⚠️ 부분 점수: '예시'를 선택했으나 구체적인 예시(커피숍 등)가 명확히 드러나지 않았습니다."
        else:
            results['Q2'] = "✅ 통과: 2가지 이상의 설명 방법이 적절히 사용되었습니다."
    else:
        results['Q2'] = "❌ 오답: 서로 다른 2가지의 설명 방법을 괄호 안에 정확히 표기해야 합니다."

    # [서논술형 3] 채점
    # 시각A: 혼자, 조용한 공간 / 청각B: 소음 배제 / 효과: 어려운 과제, 혼자 집중
    if any(k in q3_a for k in ["혼자", "1인실", "방", "독서실"]) and "친구" not in q3_a:
        res3_a = "✅ 시각 통과"
    else:
        res3_a = "❌ 시각 오답 (타인 등장 방지)"
        
    if any(k in q3_b for k in ["배제", "없애", "무음", "조용한", "연필", "백색소음"]) and "리듬감" not in q3_b:
        res3_b = "✅ 청각 통과"
    else:
        res3_b = "❌ 청각 오답 (방해되는 소음 배제 필요)"
        
    if "어려운" in q3_a_eff and "집중" in q3_a_eff and "어려운" in q3_b_eff:
        res3_eff = "✅ 효과 서술 통과 (지문 근거 명확)"
    else:
        res3_eff = "❌ 효과 서술 오답 (지문 내용 '어려운 과제 시의 조건' 누락)"
        
    results['Q3'] = f"{res3_a}\n{res3_b}\n{res3_eff}"
    return results

def grade_set_2(q1_1, q1_2, q1_3, q2, q3_a, q3_a_eff, q3_b, q3_b_eff):
    results = {}
    
    # [서논술형 1] 채점
    if "높은" in q1_1 and "고여" in q1_1: res1_1 = "✅ 정답"
    elif "고여" in q1_1: res1_1 = "⚠️ 부분 점수 ('높은'이라는 전압 비유 누락)"
    else: res1_1 = "❌ 오답"

    if any(k in q1_2 for k in ["이동하지", "머물러", "정지"]) and "흐르" not in q1_2:
        res1_2 = "✅ 정답"
    else: res1_2 = "❌ 오답 (오개념: 전하가 흐른다고 쓰면 안 됨)"

    if any(k in q1_3 for k in ["위험하지", "피해가 없", "위험성 없"]): res1_3 = "✅ 정답"
    else: res1_3 = "❌ 오답"
    
    results['Q1'] = f"- (1) {res1_1}\n- (2) {res1_2}\n- (3) {res1_3}"

    # [서논술형 2] 채점
    methods_used = re.findall(r'\((.*?)\)', q2)
    if "비유" in str(methods_used):
        results['Q2'] = "⚠️ 보류: '비유'는 1쪽 공식 설명 방법 명칭에 없으므로 교사 확인이 필요합니다."
    elif len(methods_used) >= 1:
        if "흐르" in q2 and "이동" in q2 and "머물" in q2:
            results['Q2'] = "✅ 통과: 정전기와 실생활 전기의 차이가 잘 설명되었습니다."
        else:
            results['Q2'] = "⚠️ 부분 점수: 정전기(머무름)와 실생활 전기(흐름)의 특성 대비가 부족합니다."
    else:
        results['Q2'] = "❌ 오답: 설명 방법이 괄호 안에 표기되지 않았습니다."

    # [서논술형 3] 채점
    if any(k in q3_a for k in ["높은", "댐", "산꼭대기"]) and "고여" in q3_a: res3_a = "✅ 시각 통과"
    elif "머리카락" in q3_a or "스웨터" in q3_a: res3_a = "❌ 시각 오답 ('고여 있는 물' 비유에 어긋남)"
    else: res3_a = "❌ 시각 오답"

    if any(k in q3_b for k in ["고요", "잔잔", "바람", "새소리"]): res3_b = "✅ 청각 통과"
    else: res3_b = "❌ 청각 오답"
    
    if "전압" in q3_a_eff and "위험" in q3_a_eff: res3_eff = "✅ 효과 서술 통과"
    else: res3_eff = "❌ 효과 서술 오답 (지문 근거 '전압은 높지만 위험하지 않음' 누락)"

    results['Q3'] = f"{res3_a}\n{res3_b}\n{res3_eff}"
    return results

def grade_set_3(q1_1, q1_2, q1_3, q2, q3_a, q3_a_eff, q3_b, q3_b_eff):
    results = {}
    
    # [서논술형 1] 채점
    if "로봇" in q1_1 and "완벽" in q1_1: res1_1 = "✅ 정답"
    else: res1_1 = "❌ 오답 (로봇/완벽 키워드 필요)"

    if any(k in q1_2 for k in ["감정", "철학", "이야기"]) and ("없" in q1_2 or "못" in q1_2):
        if "예술" in q1_2 and "어렵" in q1_2: res1_2 = "✅ 정답"
        else: res1_2 = "⚠️ 부분 점수 (근거는 맞으나 결론 방향 누락)"
    else: res1_2 = "❌ 오답"

    if "변화" in q1_3 and "확장" in q1_3: res1_3 = "✅ 정답"
    elif "변화" in q1_3 or "확장" in q1_3: res1_3 = "⚠️ 부분 점수 (변화/확장 중 하나만 기재됨)"
    else: res1_3 = "❌ 오답"
    
    results['Q1'] = f"- (1) {res1_1}\n- (2) {res1_2}\n- (3) {res1_3}"

    # [서논술형 2] 채점 (결론 방향 확인 필수)
    methods_used = re.findall(r'\((.*?)\)', q2)
    if len(methods_used) >= 1:
        has_negative = any(k in q2 for k in ["어렵다", "아니다", "없다"])
        has_positive = any(k in q2 for k in ["가치", "의미", "확장", "변화"])
        
        if has_negative and has_positive:
            results['Q2'] = "✅ 통과: AI 예술의 한계(예술로 보기 어려움)와 가치(상징적 의미) 결론이 모두 올바른 방향으로 서술되었습니다."
        else:
            results['Q2'] = "❌ 오답 (결론 방향 오류): 한계와 가치 중 한쪽 측면만 서술되었거나 방향성이 지문과 다릅니다."
    else:
        results['Q2'] = "❌ 오답: 설명 방법 누락"

    # [서논술형 3] 채점
    if any(k in q3_a for k in ["노력", "열정", "땀", "올림픽", "선수", "화가"]): res3_a = "✅ 시각 통과"
    else: res3_a = "❌ 시각 오답"

    if any(k in q3_b for k in ["숨소리", "박동", "따뜻", "감동"]) and "기계음" not in q3_b: res3_b = "✅ 청각 통과"
    else: res3_b = "❌ 청각 오답"
    
    if "감정" in q3_a_eff and "울림" in q3_b_eff: res3_eff = "✅ 효과 서술 통과"
    else: res3_eff = "❌ 효과 서술 오답 (추상적 표현 방지: '감정', '철학', '마음에 울림' 등 지문 용어 핈)"

    results['Q3'] = f"{res3_a}\n{res3_b}\n{res3_eff}"
    return results

# --- UI 구성 ---
tab1, tab2, tab3 = st.tabs(["[1세트] 사회적 촉진과 억제", "[2세트] 정전기의 비밀", "[3세트] 진정한 예술의 가치"])

with tab1:
    st.header("[1세트] 답변 입력")
    st.subheader("[서·논술형 1]")
    s1_q1_1 = st.text_input("1-(1) 빈칸 입력", key="s1_q1_1")
    s1_q1_2 = st.text_input("1-(2) 빈칸 입력", key="s1_q1_2")
    s1_q1_3 = st.text_input("1-(3) 빈칸 입력", key="s1_q1_3")
    
    st.subheader("[서·논술형 2]")
    s1_q2 = st.text_area("조건에 맞추어 설명문 작성 (예: ...이다. (비교와 대조))", key="s1_q2")
    
    st.subheader("[서·논술형 3]")
    s1_q3_a = st.text_input("시각 요소(Ⓐ)", key="s1_q3_a")
    s1_q3_a_eff = st.text_input("시각 요소(Ⓐ)의 효과", key="s1_q3_a_eff")
    s1_q3_b = st.text_input("청각 요소(Ⓑ)", key="s1_q3_b")
    s1_q3_b_eff = st.text_input("청각 요소(Ⓑ)의 효과", key="s1_q3_b_eff")

    if st.button("1세트 채점하기"):
        res = grade_set_1(s1_q1_1, s1_q1_2, s1_q1_3, s1_q2, s1_q3_a, s1_q3_a_eff, s1_q3_b, s1_q3_b_eff)
        st.success("채점 결과")
        st.info(f"**[서·논술형 1]**\n{res['Q1']}")
        st.info(f"**[서·논술형 2]**\n{res['Q2']}\n\n*모범 답안*\n- 비교와 대조+예시: 쉬운 과제는 타인과 함께하는 것이 좋지만, 어려운 과제는 혼자 집중하는 것이 좋다.(비교와 대조) 예를 들어, 친숙한 과목은 커피숍에서 사람들과 함께 공부하는 것이 효율적이다.(예시)")
        st.info(f"**[서·논술형 3]**\n{res['Q3']}\n\n*모범 답안*\n- Ⓐ: 독서실 1인실에서 주변을 신경 쓰지 않고 혼자 차분히 공부하는 모습\n- Ⓑ: 배경 음악 없이 조용하게 책장 넘기는 소리만 들려줌")

with tab2:
    st.header("[2세트] 답변 입력")
    # (1세트와 동일한 구조로 입력창 구성 - 코드 길이 상략 방지를 위해 핵심 입력부만 구현)
    s2_q1_1 = st.text_input("1-(1) 빈칸 입력", key="s2_q1_1")
    s2_q1_2 = st.text_input("1-(2) 빈칸 입력", key="s2_q1_2")
    s2_q1_3 = st.text_input("1-(3) 빈칸 입력", key="s2_q1_3")
    s2_q2 = st.text_area("조건에 맞추어 설명문 작성", key="s2_q2")
    s2_q3_a = st.text_input("시각 요소(Ⓐ)", key="s2_q3_a")
    s2_q3_a_eff = st.text_input("시각 요소(Ⓐ)의 효과", key="s2_q3_a_eff")
    s2_q3_b = st.text_input("청각 요소(Ⓑ)", key="s2_q3_b")
    s2_q3_b_eff = st.text_input("청각 요소(Ⓑ)의 효과", key="s2_q3_b_eff")

    if st.button("2세트 채점하기"):
        res = grade_set_2(s2_q1_1, s2_q1_2, s2_q1_3, s2_q2, s2_q3_a, s2_q3_a_eff, s2_q3_b, s2_q3_b_eff)
        st.success("채점 결과")
        st.info(f"**[서·논술형 1]**\n{res['Q1']}")
        st.info(f"**[서·논술형 2]**\n{res['Q2']}\n\n*모범 답안*\n- 대조+인과: 실생활 전기는 전하가 이동하지만, 정전기는 이동하지 않는다.(비교와 대조) 따라서 전압이 매우 높음에도 감전 위험이 없다.(인과)")
        st.info(f"**[서·논술형 3]**\n{res['Q3']}\n\n*모범 답안*\n- Ⓐ: 어마어마하게 높은 댐 위에 잔잔하게 고여 있는 호수\n- Ⓑ: 잔잔한 바람 소리나 평화로운 자연의 소리")

with tab3:
    st.header("[3세트] 답변 입력")
    s3_q1_1 = st.text_input("1-(1) 빈칸 입력", key="s3_q1_1")
    s3_q1_2 = st.text_input("1-(2) 빈칸 입력", key="s3_q1_2")
    s3_q1_3 = st.text_input("1-(3) 빈칸 입력", key="s3_q1_3")
    s3_q2 = st.text_area("조건에 맞추어 설명문 작성", key="s3_q2")
    s3_q3_a = st.text_input("시각 요소(Ⓐ)", key="s3_q3_a")
    s3_q3_a_eff = st.text_input("시각 요소(Ⓐ)의 효과", key="s3_q3_a_eff")
    s3_q3_b = st.text_input("청각 요소(Ⓑ)", key="s3_q3_b")
    s3_q3_b_eff = st.text_input("청각 요소(Ⓑ)의 효과", key="s3_q3_b_eff")

    if st.button("3세트 채점하기"):
        res = grade_set_3(s3_q1_1, s3_q1_2, s3_q1_3, s3_q2, s3_q3_a, s3_q3_a_eff, s3_q3_b, s3_q3_b_eff)
        st.success("채점 결과")
        st.info(f"**[서·논술형 1]**\n{res['Q1']}")
        st.info(f"**[서·논술형 2]**\n{res['Q2']}\n\n*모범 답안*\n- 대조+예시: AI 그림은 감정이 없어 진정한 예술로 보기 어렵다.(대조) 하지만 벨라미 사례처럼 예술 범주를 확장하는 상징적 가치가 있다.(예시)")
        st.info(f"**[서·논술형 3]**\n{res['Q3']}\n\n*모범 답안*\n- Ⓐ: 수없이 넘어지면서도 다시 일어나는 피겨 선수의 표정 클로즈업\n- Ⓑ: 거칠지만 인간적인 숨소리나 따뜻한 배경 음악")