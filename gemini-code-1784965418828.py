import streamlit as st
import re

# --- 페이지 설정 ---
st.set_page_config(page_title="서논술형 실전 적용 학습 시스템", layout="wide")

# 세션 상태 초기화
if 'menu' not in st.session_state:
    st.session_state.menu = "사회적 촉진"
if 'sub_menu_1' not in st.session_state:
    st.session_state.sub_menu_1 = "1번 빈칸 채우기"
if 'sub_menu_2' not in st.session_state:
    st.session_state.sub_menu_2 = "1번 빈칸 채우기"
if 'sub_menu_3' not in st.session_state:
    st.session_state.sub_menu_3 = "1번 빈칸 채우기"

# --- 상단 메인 메뉴바 (화면 상단 디자인 반영) ---
menu_selection = st.radio(
    "상단 메뉴",
    ["🔥 사회적 촉진", "⚡ 정전기", "🎨 인공지능 예술", "📚 복습한 내용"],
    horizontal=True,
    label_visibility="collapsed"
)

if "사회적 촉진" in menu_selection:
    st.session_state.menu = "사회적 촉진"
elif "정전기" in menu_selection:
    st.session_state.menu = "정전기"
elif "인공지능 예술" in menu_selection:
    st.session_state.menu = "인공지능 예술"
elif "복습한 내용" in menu_selection:
    st.session_state.menu = "복습한 내용"

st.markdown("---")

# =====================================================================
# 📚 복습한 내용 화면 (PDF 1쪽 핵심 지식)
# =====================================================================
if st.session_state.menu == "복습한 내용":
    st.header("📚 핵심 지식 복습하기")
    st.markdown("### 1. 다양한 설명 방법 (설명하는 글 쓰기)")
    st.markdown("""
    * **정의**: 대상의 뜻, 개념 등을 밝힐 때 (예: 우정이란 친구 사이의 정을 말한다.)[cite: 1]
    * **예시**: 구체적인 예를 바탕으로 대상을 설명할 때 (예: 콩을 원료로 만든 식품의 예로는 두부, 메주, 된장 등이 있다.)[cite: 1]
    * **인과**: 원인과 결과를 중심으로 대상을 설명할 때 (예: 올해는 비가 거의 오지 않아서 흉년이 들었다.)[cite: 1]
    * **분석**: 여러 요소나 부분으로 이루어진 대상을 설명할 때 (예: 곤충의 몸은 머리, 가슴, 배의 세 부분으로 이루어져 있다.)[cite: 1]
    * **비교와 대조**: 둘 이상의 대상의 공통점과 차이점을 드러낼 때[cite: 1]
    * **분류와 구분**: 대상을 기준에 따라 그 종류를 묶거나 나눌 때[cite: 1]
    """)
    st.markdown("### 2. 매체의 복합양식성과 영상 매체 자료 제작")
    st.markdown("""
    * **복합양식성**: 문자, 소리, 그림, 사진, 동영상 등 다양한 양식이 결합된 것 (영상 매체 자료에서 두드러짐)[cite: 1]
    * **유의할 점**: 복합양식성 고려, 주제와 목적·예상 시청자 고려[cite: 1]
    * **스토리보드 구성**: 화면(시각 요소), 자막, 장면, 소리(청각 요소 - 효과음, 배경음악) 등[cite: 1]
    """)

# =====================================================================
# 💡 1세트: 사회적 촉진과 억제 화면
# =====================================================================
elif st.session_state.menu == "사회적 촉진":
    st.markdown("## 💡 [실전 적용 1] 과제 난이도와 사회적 촉진/억제")
    
    # 지문 박스
    st.info("""
    **[기자]** 심리학 용어인 '사회적 촉진'과 '사회적 억제'를 일상생활, 특히 우리의 학습에 어떻게 적용할 수 있을까요?  
    **[전문가]** 이 두 가지 개념을 알면 상황에 맞춰 유용하게 활용할 수 있습니다. 예를 들어, 비교적 쉬운 취미 생활이나 큰 노력을 들일 필요가 없는 과제를 할 때는 어떨까요?  
    **[기자]** 음, 그냥 집에서 편하게 혼자 하는 게 집중이 잘되지 않을까요?  
    **[전문가]** 그렇지 않습니다. 오히려 집에서 혼자 하는 것보다는 커피숍이나 도서관에서 하는 것이 더 효율적일 수 있습니다. 평소 친숙하고 좋아하는 과목이라면 공부 모임을 만들어서 다른 사람들과 함께 공부하는 것도 좋은 방법이죠.  
    **[기자]** 그렇다면 어렵고 복잡한 과제를 할 때는 어떻게 해야 하나요?  
    **[전문가]** 그럴 때는 반대입니다. 지나치게 어렵거나 도전이 필요한 과제는 충분히 연습하며 익숙해질 때까지 차분하게 혼자 집중하는 시간을 가지는 것이 좋습니다.
    """)
    
    # 세부 문항 전환 버튼 (스크린샷 UI 맞춤)
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("✏️ 1번 빈칸 채우기", use_container_width=True, type="primary" if st.session_state.sub_menu_1 == "1번 빈칸 채우기" else "secondary"):
            st.session_state.sub_menu_1 = "1번 빈칸 채우기"
            st.rerun()
    with col2:
        if st.button("✏️ 2번 설명문 쓰기", use_container_width=True, type="primary" if st.session_state.sub_menu_1 == "2번 설명문 쓰기" else "secondary"):
            st.session_state.sub_menu_1 = "2번 설명문 쓰기"
            st.rerun()
    with col3:
        if st.button("🎬 3번 영상 기획", use_container_width=True, type="primary" if st.session_state.sub_menu_1 == "3번 영상 기획" else "secondary"):
            st.session_state.sub_menu_1 = "3번 영상 기획"
            st.rerun()
            
    st.markdown("---")
    
    if st.session_state.sub_menu_1 == "1번 빈칸 채우기":
        st.markdown("**[서·논술형 1]** 윗글을 요약하여 표로 정리하였다. 빈칸 ㉠~㉢에 들어갈 내용을 찾아 쓰시오[cite: 1].")
        
        st.markdown("""
        | 과제의 특성 | 환경 | 현상 |
        | :--- | :--- | :--- |
        | ㉠[cite: 1] | 공부 모임 등 여럿이 함께함[cite: 1] | 사회적 촉진[cite: 1] |
        | 어려운 과제[cite: 1] | ㉡[cite: 1] | ㉢[cite: 1] |
        """)
        
        s1_1 = st.text_input("(1) ㉠에 들어갈 내용:", placeholder="비교적 쉬운 과제나 취미 등")
        s1_2 = st.text_input("(2) ㉡에 들어갈 내용:", placeholder="차분하고 혼자 집중하기")
        s1_3 = st.text_input("(3) ㉢에 들어갈 내용:", placeholder="사회적 억제")
        
        if st.button("제출하고 피드백 받기", key="btn_s1_1"):
            errs = []
            if not any(k in s1_1 for k in ["쉬운", "노력", "친숙"]): errs.append("(1) 빈칸 내용 확인 필요")
            if not any(k in s1_2 for k in ["혼자", "집중", "차분"]): errs.append("(2) 빈칸 내용 확인 필요")
            if "억제" not in s1_3: errs.append("(3) 빈칸 내용 확인 필요")
            
            if not errs:
                st.success("🎉 정답입니다! 훌륭합니다.")
            else:
                st.error(f"⚠️ 일부 수정이 필요합니다: {', '.join(errs)}")
                st.markdown("**[모범 답안 참고]**\n- (1) 비교적 쉬운 취미 생활, 큰 노력을 들일 필요가 없는 과제[cite: 1]\n- (2) 충분히 연습하며 익숙해질 때까지 차분하게 혼자 집중하는 시간을 가짐[cite: 1]\n- (3) 사회적 억제[cite: 1]")

    elif st.session_state.sub_menu_1 == "2번 설명문 쓰기":
        st.markdown("**[서·논술형 2]** 윗글을 활용하여 '과제 난이도에 따른 효율적인 학습 전략'에 대한 설명문을 작성하려 한다. 주어진 첫 문장에 이어지는 내용을 <조건>에 맞추어 작성하시오[cite: 1].")
        st.markdown("""
        > **<조건>**[cite: 1]
        > * 주어진 문장에 이어지는 문장을 (1), (2)에 각각 하나씩 작성할 것[cite: 1].
        > * (1)과 (2)에는 서로 다른 2가지의 설명 방법을 사용하여, 각 문장 끝에 사용된 설명 방법의 명칭을 괄호에 넣어 표기할 것[cite: 1].
        > * 윗글에 제시된 내용만을 활용할 것[cite: 1].
        """)
        st.markdown("첫 문장: 과제의 특성과 난이도에 따라 우리의 학습 효율을 높이는 방법은 다르게 적용되어야 한다[cite: 1].")
        
        s2_1 = st.text_area("(1) 첫 번째 문장:", placeholder="문장 끝에 (설명방법)을 적으세요.")
        s2_2 = st.text_area("(2) 두 번째 문장:", placeholder="문장 끝에 (설명방법)을 적으세요.")
        
        if st.button("제출하고 피드백 받기", key="btn_s1_2"):
            methods = re.findall(r'\((.*?)\)', s2_1 + s2_2)
            valid_m = ["정의", "예시", "인과", "분석", "비교", "대조", "분류", "구분"]
            found = [m for m in methods if any(v in m for v in valid_m)]
            
            if len(set(found)) >= 2:
                st.success("🎉 조건 충족! 훌륭하게 설명문을 작성했습니다.")
            else:
                st.warning("⚠️ 서로 다른 2가지 이상의 설명 방법 명칭을 괄호 안에 정확히 기재했는지 확인해 주세요.")
                st.markdown("**[모범 답안 예시]**\n- (1) 비교적 쉬운 과제는 타인과 함께하는 것이 좋지만, 어려운 과제는 혼자 집중하는 것이 좋다. (비교와 대조)[cite: 1]\n- (2) 예를 들어, 친숙한 과목은 커피숍에서 사람들과 함께 공부하는 것이 효율적이다. (예시)[cite: 1]")

    elif st.session_state.sub_menu_1 == "3번 영상 기획":
        st.markdown("**[서·논술형 3]** 윗글을 바탕으로 '상황에 맞는 학습 공간 선택법'을 설명하는 영상을 제작하려 한다. 기획안의 빈칸 Ⓐ, Ⓑ를 채우고 효과를 서술하시오[cite: 1].")
        
        q3_a = st.text_input("(1) 시각 요소 (Ⓐ):", placeholder="어려운 과제를 할 때의 시각적 연출 계획[cite: 1]")
        q3_a_eff = st.text_area("시각 요소 (Ⓐ)의 효과:", placeholder="지문 내용을 근거로 효과 서술[cite: 1]")
        q3_b = st.text_input("(2) 청각 요소 (Ⓑ):", placeholder="어려운 과제를 할 때의 청각적 연출 계획[cite: 1]")
        q3_b_eff = st.text_area("청각 요소 (Ⓑ)의 효과:", placeholder="지문 내용을 근거로 효과 서술[cite: 1]")
        
        if st.button("제출하고 피드백 받기", key="btn_s1_3"):
            if any(k in q3_a for k in ["혼자", "독서실", "방", "1인실"]) and any(k in q3_b for k in ["조용", "배제", "무음", "백색소음"]):
                st.success("🎉 훌륭한 영상 기획입니다! 조건에 부합합니다.")
            else:
                st.info("💡 피드백: 어려운 과제 시 필요한 '혼자 차분하게 집중하는 환경'과 '소음 배제'의 특성이 Ⓐ와 Ⓑ에 잘 드러나도록 수정해 보세요[cite: 1].")
                st.markdown("**[모범 답안 예시]**\n- Ⓐ: 독서실 1인실에서 주변을 신경 쓰지 않고 혼자 차분히 공부하는 모습[cite: 1]\n- Ⓑ: 배경 음악 없이 조용하게 책장 넘기는 소리만 들려줌[cite: 1]")

# =====================================================================
# ⚡ 2세트: 정전기 화면
# =====================================================================
elif st.session_state.menu == "정전기":
    st.markdown("## ⚡ [실전 적용 2] 전압은 높지만 위험하지 않은 정전기의 비밀")
    
    st.info("""
    **[기자]** 겨울철 불청객인 '정전기'란 정확히 무엇인지 설명 부탁드립니다.  
    **[전문가]** 정전기란 전하가 정지 상태로 있어 그 분포가 시간적으로 변화하지 않는 전기, 그리고 그로 인한 전기 현상을 말합니다. 쉽게 설명하면 흐르지 않고 머물러 있는 전기라고 해서 "움직이지 아니하여 조용하다."는 뜻을 가진 한자 '정(靜)'을 써서 정전기라고 부르는 것이죠[cite: 1].  
    **[기자]** 우리가 실생활에서 쓰는 전기와는 어떻게 다른가요? 물에 비유해서 설명해 주시면 이해가 쉬울 것 같습니다[cite: 1].  
    **[전문가]** 아주 좋은 비유가 될 수 있습니다. 우리가 실생활에서 쓰는 전기가 '흐르는 물'이라면, 정전기는 '높은 곳에 고여 있는 물'이라고 할 수 있습니다[cite: 1].  
    **[기자]** 정전기가 일어날 때 찌릿한 느낌이 드는데, 혹시 위험하지는 않은가요?  
    **[전문가]** 정전기의 전압은 매우 높지만, 우리가 실생활에서 쓰는 전기와는 다르게 전하가 이동하지 않고 머물러 있어 위험하지는 않습니다. 어마어마하게 높은 곳에 고여 있는 물이지만 떨어지지 않고 있어서 별 피해가 없는 것과 같다고 이해하시면 됩니다[cite: 1].
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("✏️ 1번 빈칸 채우기", use_container_width=True, type="primary" if st.session_state.sub_menu_2 == "1번 빈칸 채우기" else "secondary"):
            st.session_state.sub_menu_2 = "1번 빈칸 채우기"
            st.rerun()
    with col2:
        if st.button("✏️ 2번 설명문 쓰기", use_container_width=True, type="primary" if st.session_state.sub_menu_2 == "2번 설명문 쓰기" else "secondary"):
            st.session_state.sub_menu_2 = "2번 설명문 쓰기"
            st.rerun()
    with col3:
        if st.button("🎬 3번 영상 기획", use_container_width=True, type="primary" if st.session_state.sub_menu_2 == "3번 영상 기획" else "secondary"):
            st.session_state.sub_menu_2 = "3번 영상 기획"
            st.rerun()
            
    st.markdown("---")
    
    if st.session_state.sub_menu_2 == "1번 빈칸 채우기":
        st.markdown("**[서·논술형 1]** 윗글을 요약하여 표로 정리하였다. 빈칸에 들어갈 내용을 찾아 쓰시오[cite: 1].")
        st.markdown("""
        | 대상 | 물의 상태에 비유 | 전하의 상태 | 위험성 |
        | :--- | :--- | :--- | :--- |
        | 실생활 전기[cite: 1] | 흐르는 물[cite: 1] | 전하가 이동함[cite: 1] | 감전 등의 위험이 있음[cite: 1] |
        | 정전기[cite: 1] | ㉠[cite: 1] | ㉡[cite: 1] | ㉢[cite: 1] |
        """)
        s2_q1_1 = st.text_input("(1) ㉠에 들어갈 내용:", placeholder="높은 곳에 고여 있는 물")
        s2_q1_2 = st.text_input("(2) ㉡에 들어갈 내용:", placeholder="전하가 이동하지 않고 머물러 있음")
        s2_q1_3 = st.text_input("(3) ㉢에 들어갈 내용:", placeholder="위험하지 않음")
        
        if st.button("제출하고 피드백 받기", key="btn_s2_1"):
            if "고여" in s2_q1_1 and ("머물" in s2_q1_2 or "이동하지" in s2_q1_2) and "위험" in s2_q1_3:
                st.success("🎉 정답입니다!")
            else:
                st.error("⚠️ 빈칸 내용을 다시 확인해 보세요.")
                st.markdown("**[모범 답안]**\n- (1) 높은 곳에 고여 있는 물[cite: 1]\n- (2) 전하가 이동하지 않고 머물러 있음[cite: 1]\n- (3) 위험하지 않음 (또는 별 피해가 없음)[cite: 1]")

    elif st.session_state.sub_menu_2 == "2번 설명문 쓰기":
        st.markdown("**[서·논술형 2]** 윗글을 활용하여 '정전기의 특징'에 대한 설명문을 작성하시오[cite: 1].")
        st.markdown("첫 문장: 겨울철에 흔히 겪는 정전기는 우리가 평소 집에서 사용하는 전기와는 다른 뚜렷한 특징이 있다[cite: 1].")
        s2_m1 = st.text_area("(1) 첫 번째 문장:", placeholder="문장 끝에 (설명방법) 기재")
        s2_m2 = st.text_area("(2) 두 번째 문장:", placeholder="문장 끝에 (설명방법) 기재")
        if st.button("제출하고 피드백 받기", key="btn_s2_2"):
            st.success("✨ 제출 완료되었습니다. 서로 다른 설명 방법과 정전기 특징(머무름, 위험 없음)이 잘 드러났는지 확인해 보세요[cite: 1].")
            st.markdown("**[모범 답안 예시]**\n- (1) 실생활 전기는 전하가 이동하지만, 정전기는 전하가 이동하지 않고 머물러 있다. (비교와 대조)[cite: 1]\n- (2) 따라서 전압은 높지만 감전 등의 위험이 발생하지 않는다. (인과)[cite: 1]")

    elif st.session_state.sub_menu_2 == "3번 영상 기획":
        st.markdown("**[서·논술형 3]** 정전기의 특징을 설명하는 영상 기획안의 Ⓐ, Ⓑ 연출 계획을 세우고 효과를 서술하시오[cite: 1].")
        s2_a = st.text_input("(1) 시각 요소 (Ⓐ) - 정전기(고여 있는 물):")
        s2_a_eff = st.text_area("시각 요소 (Ⓐ)의 효과:")
        s2_b = st.text_input("(2) 청각 요소 (Ⓑ):")
        s2_b_eff = st.text_area("청각 요소 (Ⓑ)의 효과:")
        if st.button("제출하고 피드백 받기", key="btn_s2_3"):
            st.success("✨ 제출 완료! '높은 곳에 고여 있는 물' 비유와 '정(靜)의 의미'가 잘 담겼는지 확인하세요[cite: 1].")
            st.markdown("**[모범 답안 예시]**\n- Ⓐ: 어마어마하게 높은 댐 위에 잔잔하게 고여 있는 거대한 호수의 모습[cite: 1]\n- Ⓑ: 잔잔한 바람 소리나 평화로운 자연의 소리[cite: 1]")

# =====================================================================
# 🎨 3세트: 인공지능 예술 화면
# =====================================================================
elif st.session_state.menu == "인공지능 예술":
    st.markdown("## 🎨 [실전 적용 3] 인공 지능이 그린 그림을 바라보는 시각")
    
    st.info("""
    **[기자]** 최근 생성형 인공 지능이 그린 그림이 미술계에서 큰 화제를 모으고 있습니다. 어떤 작품인지 소개해 주실 수 있을까요?[cite: 1]  
    **[전문가]** 네, 대표적으로 「에드몽 드 벨라미」라는 작품이 있습니다. 이 작품은 14~20세기에 그려진 초상화 1만 5,000점을 토대로 알고리즘과 데이터를 사용해 그려졌습니다. 뉴욕 크리스티 경매에서 최종 낙찰가 43만 2,000달러에 판매되어 큰 놀라움을 주었죠[cite: 1].  
    **[기자]** 그렇다면 이 그림을 인간이 만든 예술 작품과 같다고 볼 수 있을까요?[cite: 1]  
    **[전문가]** 올림픽 경기를 예로 들어 볼게요. 우리가 올림픽에 열광하는 이유는 선수들이 경기를 위해 기울인 노력이나 열정을 알기 때문입니다. 반면 로봇이 한 번의 실수 없이 완벽하게 피겨 스케이팅을 해내더라도 우리의 마음을 울리지는 못하지요. 이처럼 인간의 작품에는 작가의 고유한 감정이나 철학, 그리고 작가가 살아온 삶의 경험, 세상을 바라보는 관점, 그를 둘러싼 환경 같은 내외부적인 요소가 종합적으로 담겨 있으므로 예술로 볼 수 있습니다. 하지만 인공 지능은 감정도 느끼지 못하고 독자적인 철학이나 이야기가 없기 때문에 이를 예술로 보기는 어렵습니다[cite: 1].  
    **[기자]** 그렇다면 인공 지능이 그린 그림은 가치가 전혀 없는 것인가요?[cite: 1]  
    **[전문가]** 그렇지는 않습니다. 비록 인간과 같은 감정은 없더라도, 기존 미술계에 큰 변화를 가져왔다는 점에서 분명한 의미가 있습니다. 또한 앞으로 우리가 알고 있던 예술의 범주를 확장할 수 있다는 점에서 상징적인 가치를 지닙니다[cite: 1].
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("✏️ 1번 빈칸 채우기", use_container_width=True, type="primary" if st.session_state.sub_menu_3 == "1번 빈칸 채우기" else "secondary"):
            st.session_state.sub_menu_3 = "1번 빈칸 채우기"
            st.rerun()
    with col2:
        if st.button("✏️ 2번 설명문 쓰기", use_container_width=True, type="primary" if st.session_state.sub_menu_3 == "2번 설명문 쓰기" else "secondary"):
            st.session_state.sub_menu_3 = "2번 설명문 쓰기"
            st.rerun()
    with col3:
        if st.button("🎬 3번 영상 기획", use_container_width=True, type="primary" if st.session_state.sub_menu_3 == "3번 영상 기획" else "secondary"):
            st.session_state.sub_menu_3 = "3번 영상 기획"
            st.rerun()
            
    st.markdown("---")
    
    if st.session_state.sub_menu_3 == "1번 빈칸 채우기":
        st.markdown("**[서·논술형 1]** 윗글을 요약하여 표로 정리하였다. 빈칸에 들어갈 내용을 쓰시오[cite: 1].")
        st.markdown("""
        | 대상 | 올림픽 경기에 비유 | 예술로 볼 수 있는가 | 예술로서의 가치 |
        | :--- | :--- | :--- | :--- |
        | 인간의 예술[cite: 1] | 인간 선수의 노력과 열정이 담긴 올림픽 경기[cite: 1] | 작가의 경험, 관점 등이 담겨 있으므로 예술이다.[cite: 1] | 감상자에게 남다른 감동을 줌[cite: 1] |
        | 인공 지능의 예술[cite: 1] | ㉠[cite: 1] | ㉡[cite: 1] | ㉢[cite: 1] |
        """)
        s3_q1_1 = st.text_input("(1) ㉠에 들어갈 내용:", placeholder="로봇이 완벽하게 해내는 피겨 스케이팅")
        s3_q1_2 = st.text_input("(2) ㉡에 들어갈 내용:", placeholder="감정과 철학이 없어 예술로 보기 어렵다")
        s3_q1_3 = st.text_input("(3) ㉢에 들어갈 내용:", placeholder="미술계 변화, 예술 범주 확장")
        
        if st.button("제출하고 피드백 받기", key="btn_s3_1"):
            if "로봇" in s3_q1_1 and ("감정" in s3_q1_2 or "철학" in s3_q1_2) and ("변화" in s3_q1_3 or "확장" in s3_q1_3):
                st.success("🎉 정답입니다!")
            else:
                st.error("⚠️ 빈칸 내용을 다시 확인해 보세요.")
                st.markdown("**[모범 답안]**\n- (1) 로봇이 한 번의 실수 없이 완벽하게 해내는 피겨 스케이팅[cite: 1]\n- (2) 감정도 느끼지 못하고 독자적인 철학이나 이야기가 없기 때문에 예술로 보기 어렵다[cite: 1].\n- (3) 기존 미술계에 큰 변화를 가져왔고, 예술의 범주를 확장할 수 있다[cite: 1].")

    elif st.session_state.sub_menu_3 == "2번 설명문 쓰기":
        st.markdown("**[서·논술형 2]** 인공 지능이 그린 그림을 바라보는 시각에 대한 설명문을 작성하시오[cite: 1].")
        st.markdown("첫 문장: 인공 지능이 그린 그림이 늘어나는 요즘, 우리는 이 작품들을 어떤 눈으로 바라봐야 할지 올바르게 생각해야 한다[cite: 1].")
        s3_m1 = st.text_area("(1) 첫 번째 문장:", placeholder="문장 끝에 (설명방법) 기재")
        s3_m2 = st.text_area("(2) 두 번째 문장:", placeholder="문장 끝에 (설명방법) 기재")
        if st.button("제출하고 피드백 받기", key="btn_s3_2"):
            st.success("✨ 제출 완료되었습니다. AI 예술의 한계와 상징적 가치가 모두 올바르게 서술되었는지 확인해 보세요[cite: 1].")
            st.markdown("**[모범 답안 예시]**\n- (1) 인간의 작품에는 감정과 철학이 담겨 있지만, 인공 지능은 감정이나 이야기가 없어 예술로 보기는 어렵다. (비교와 대조)[cite: 1]\n- (2) 하지만 벨라미 사례처럼 기존 미술계에 큰 변화를 주고 예술의 범주를 확장한다는 점에서 상징적 가치가 있다. (예시)[cite: 1]")

    elif st.session_state.sub_menu_3 == "3번 영상 기획":
        st.markdown("**[서·논술형 3]** 인공 지능이 그린 그림을 바라보는 시각을 설명하는 영상 기획안의 Ⓐ, Ⓑ 연출 계획을 세우고 효과를 서술하시오[cite: 1].")
        s3_a = st.text_input("(1) 시각 요소 (Ⓐ) - 진정한 예술:")
        s3_a_eff = st.text_area("시각 요소 (Ⓐ)의 효과:")
        s3_b = st.text_input("(2) 청각 요소 (Ⓑ):")
        s3_b_eff = st.text_area("청각 요소 (Ⓑ)의 효과:")
        if st.button("제출하고 피드백 받기", key="btn_s3_3"):
            st.success("✨ 제출 완료! 인간의 노력, 감정, 마음에 주는 울림이 잘 표현되었는지 확인하세요[cite: 1].")
            st.markdown("**[모범 답안 예시]**\n- Ⓐ: 경기 중 수없이 넘어지면서도 다시 일어나 연기하는 피겨 선수의 표정 클로즈업[cite: 1]\n- Ⓑ: 거칠지만 인간적인 숨소리나 벅찬 감동을 주는 따뜻한 배경 음악[cite: 1]")
