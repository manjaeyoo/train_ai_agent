import streamlit as st
from prompt_chaining import prompt_chain_workflow, default_prompts

# 메인 함수 선언 및 페이지 설정
def main():
    st.set_page_config(page_title="프롬프트 체이닝 에이전트", layout="wide")
    st.title("프롬프트 체이닝 에이전트(여행 일정 수립)")

    # 텍스트 입력창 생성
    initial_input = st.text_area(
        "여행 스타일 입력",
        value = """따뜻한 날씨를 좋아하고 자연 경관과 역사적인 장소를 둘러보는 걸 선호해."""
    )

    # 단계별 프롬프트 설정창 생성
    custom_prompts = []
    with st.expander("⚙ 단계별 프롬프트 설정", expanded=False):
        for i, default_prompt in enumerate(default_prompts, 1):
            edited = st.text_area(
                f"프롬프트 {i}",
                value = default_prompt,
                height = 140,
                key = f"prompt_{i}"
            )
            custom_prompts.append(edited)

    # 프롬프트 체인 실행 
    if st.button("🚀 프롬프트 체인 실행"):
        final_result_tab, details_tab = st.tabs(["✨ 최종 결과", "🔄 세부 단계"])
        with st.spinner("실행 중입니다..."):
            results, final_prompts = prompt_chain_workflow(initial_input, custom_prompts)
        # 결과 표시
        with final_result_tab:
            st.write(results[-1])
        with details_tab:
            for i in range(len(custom_prompts)):
                with st.expander(f"📝 {i+1} 단계: 프롬프트와 응답", expanded=False):
                    st.markdown(f"===== 프롬프트 =====")
                    st.code(final_prompts[i])
                    st.markdown(f"===== 응답 =====")
                    st.write(results[i])


if __name__ == "__main__":
    main()
