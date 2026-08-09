import streamlit as st

# 1. Page Configuration - Centered Mobile App Layout
st.set_page_config(
    page_title="MDR4T - MDR-TB Guide for Thai",
    page_icon=None,
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Minimalist Mobile UI Styling (Strict 3-Color Palette)
# Color 1: #1E293B (Dark Slate - Text & Primary Headers)
# Color 2: #0F766E (Teal - Primary Accent & Recommendation Highlight)
# Color 3: #F8FAFC (Light Neutral - Backgrounds & Card Container Base)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Prompt', -apple-system, BlinkMacSystemFont, sans-serif;
        background-color: #f8fafc;
        color: #1e293b;
    }
    
    /* Hide Streamlit Header & Footer elements for clean mobile app look */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Mobile Outer Shell Container */
    .stAppViewContainer {
        background-color: #f8fafc;
    }

    .main .block-container {
        max-width: 520px;
        padding-top: 1rem;
        padding-bottom: 2rem;
        padding-left: 1rem;
        padding-right: 1rem;
        margin: 0 auto;
    }
    
    /* Minimal App Header */
    .mobile-header {
        text-align: center;
        padding: 1.2rem 1rem 0.8rem 1rem;
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        margin-bottom: 1rem;
    }
    
    .mobile-header h1 {
        font-size: 1.6rem;
        font-weight: 700;
        color: #1e293b;
        margin: 0;
        letter-spacing: -0.5px;
    }

    .mobile-header p {
        font-size: 0.85rem;
        color: #0f766e;
        font-weight: 500;
        margin-top: 0.2rem;
        margin-bottom: 0;
    }

    /* Minimal Card Containers */
    .min-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1rem 1.2rem;
        margin-bottom: 0.8rem;
    }

    @media (prefers-color-scheme: dark) {
        .mobile-header, .min-card {
            background: #1e293b;
            border-color: #334155;
            color: #f8fafc;
        }
        .mobile-header h1 {
            color: #f8fafc;
        }
        .mobile-header p {
            color: #2dd4bf;
        }
    }

    .section-title {
        font-size: 0.95rem;
        font-weight: 600;
        color: #1e293b;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.6rem;
    }

    @media (prefers-color-scheme: dark) {
        .section-title {
            color: #cbd5e1;
        }
    }

    /* Minimal Pattern Badge */
    .min-badge {
        display: inline-block;
        padding: 0.4rem 0.8rem;
        border-radius: 6px;
        font-weight: 600;
        font-size: 0.95rem;
        background-color: #f1f5f9;
        color: #1e293b;
        border: 1px solid #cbd5e1;
    }

    /* Minimal Formula Highlight Box */
    .min-formula-box {
        background-color: #0f766e;
        color: #ffffff;
        padding: 1rem;
        border-radius: 8px;
        font-size: 1.4rem;
        font-weight: 700;
        text-align: center;
        letter-spacing: 0.5px;
        margin-top: 0.4rem;
    }

    /* Minimal Disclaimer Box */
    .min-disclaimer {
        font-size: 0.78rem;
        color: #64748b;
        border-top: 1px solid #e2e8f0;
        padding-top: 1rem;
        margin-top: 1.5rem;
        text-align: justify;
        line-height: 1.4;
    }
</style>
""", unsafe_allow_html=True)

# 3. Minimal Mobile App Header
st.markdown("""
<div class="mobile-header">
    <h1>MDR4T</h1>
    <p>โปรแกรมช่วยเลือกสูตรการรักษาวัณโรคปอดดื้อยา</p>
</div>
""", unsafe_allow_html=True)

# 4. Logic Functions (Identical logic)
def calculate_resistance_pattern(H, R, Q, A):
    if H and not R:
        return "Rifampicin-susceptible, INH-resistant (Hr-TB)"
    elif not H and R:
        if Q == "not resist":
            return "RR-TB"
        elif Q == "not known":
            return "RR-TB, FQ susceptibility pending"
        elif Q == "resist":
            return "XDR-TB" if A else "Pre-XDR-TB"
    elif H and R:
        if Q == "not resist":
            return "MDR-TB"
        elif Q == "not known":
            return "MDR-TB, FQ susceptibility pending"
        elif Q == "resist":
            return "XDR-TB" if A else "Pre-XDR-TB"
    elif R and Q == "resist":
        return "XDR-TB" if A else "Pre-XDR-TB"
    else:
        return "ไม่พบรูปแบบดื้อยาเฉพาะ (Susceptible / Pending)"

def calculate_recommended_formula(H, R, Q, A, kid, pregnant):
    if H and not R:
        if Q in ["not resist", "not known"]:
            return "6REZLfx หรือ 6(H)REZLfx"
        elif Q == "resist":
            return "6REZ หรือ 6(H)REZ"
    elif R:
        if Q == "resist":
            if A:
                return "Longer 18-m regimen"
            else:
                return "6BDLC" if (kid or pregnant) else "6BPAL"
        else:
            return "6BDLLfx" if (kid or pregnant) else "6BPaLM"
                
    return "โปรดระบุข้อมูลการดื้อยา"

# 5. Mobile App Form Inputs (Minimal Stack)
with st.container():
    st.markdown('<div class="section-title">1. ประวัติการดื้อยา</div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.caption("ผลความไวต่อยา (DST)")
        c1, c2 = st.columns(2)
        with c1:
            h_resist = st.checkbox("Isoniazid (H)", value=False)
        with c2:
            r_resist = st.checkbox("Rifampicin (R)", value=False)
        
        st.markdown("---")
        st.caption("Fluoroquinolone (FQ)")
        fq_status = st.radio(
            "FQ Status",
            options=["not known", "not resist", "resist"],
            format_func=lambda x: {
                "not known": "ไม่ทราบผล / รอผล",
                "not resist": "ไม่ดื้อยา",
                "resist": "ดื้อยา"
            }[x],
            index=0,
            label_visibility="collapsed"
        )
        
        group_a_resist = False
        if fq_status == "resist":
            st.markdown("---")
            group_a_resist = st.checkbox("ดื้อยา Group A (Bedaquiline / Linezolid)", value=False)

with st.container():
    st.markdown('<div class="section-title">2. ลักษณะผู้ป่วย</div>', unsafe_allow_html=True)
    with st.container(border=True):
        is_kid = st.checkbox("อายุน้อยกว่า 14 ปี", value=False)
        is_pregnant = st.checkbox("ตั้งครรภ์ หรือ ให้นมบุตร", value=False)

# Calculations
pattern_text = calculate_resistance_pattern(h_resist, r_resist, fq_status, group_a_resist)
recommended_formula = calculate_recommended_formula(h_resist, r_resist, fq_status, group_a_resist, is_kid, is_pregnant)

# 6. Minimal Results Section
st.markdown('<div class="section-title">3. ผลการวิเคราะห์</div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="min-card">
    <div style="font-size: 0.8rem; color: #64748b; margin-bottom: 0.3rem;">รูปแบบการดื้อยา</div>
    <div class="min-badge">{pattern_text}</div>
    <div style="font-size: 0.8rem; color: #64748b; margin-top: 0.8rem; margin-bottom: 0.2rem;">สูตรยาที่แนะนำ</div>
    <div class="min-formula-box">{recommended_formula}</div>
</div>
""", unsafe_allow_html=True)

# 7. Regimen Details & Clinical Note (Minimal Expanders)
with st.expander("รายละเอียดส่วนประกอบสูตรยา"):
    if "6BPaLM" in recommended_formula:
        st.markdown("**6BPaLM**: Bedaquiline + Pretomanid + Linezolid + Moxifloxacin (6 เดือน)")
    elif "6BPAL" in recommended_formula:
        st.markdown("**6BPAL**: Bedaquiline + Pretomanid + Linezolid (6 เดือน)")
    elif "6BDLLfx" in recommended_formula:
        st.markdown("**6BDLLfx**: Bedaquiline + Delamanid + Linezolid + Levofloxacin (6 เดือน)")
    elif "6BDLC" in recommended_formula:
        st.markdown("**6BDLC**: Bedaquiline + Delamanid + Linezolid + Clofazimine (6 เดือน)")
    elif "6REZ" in recommended_formula:
        st.markdown("**6REZ / 6REZLfx**: Rifampicin + Ethambutol + Pyrazinamide ± Levofloxacin")
    elif "Longer" in recommended_formula:
        st.markdown("**Longer 18-m regimen**: สูตรยารักษาระยะยาว (18 เดือนขึ้นไป)")
    else:
        st.write("เลือกข้อมูลการดื้อยาเพื่อดูรายละเอียด")

with st.expander("ข้อความสรุปสำหรับบันทึกเวชระเบียน"):
    fq_th = {"not known": "ไม่ทราบผล", "not resist": "ไม่ดื้อยา", "resist": "ดื้อยา"}[fq_status]
    summary_text = (
        f"MDR4T Summary:\n"
        f"• DST: H={h_resist}, R={r_resist}, FQ={fq_th}"
        + (f", Group A={group_a_resist}" if fq_status == "resist" else "") + "\n"
        f"• Patient: Age<14={is_kid}, Pregnant/Lactating={is_pregnant}\n"
        f"• Pattern: {pattern_text}\n"
        f"• Regimen: {recommended_formula}\n"
        f"Ref: WHO TB Handbook 2025"
    )
    st.code(summary_text, language="text")

# 8. Reference Dosing & Drug Groups (Minimal Segmented Control)
st.markdown('<div class="section-title">4. ข้อมูลยาอ้างอิง</div>', unsafe_allow_html=True)

view_dose = st.checkbox("แสดงขนาดยาและกลุ่มยาอ้างอิง", value=False)

if view_dose:
    tab_dose, tab_9m, tab_longer = st.tabs(["ขนาดยา", "9-Month", "Longer"])
    
    with tab_dose:
        st.markdown("""
        **ขนาดยาผู้ใหญ่:**
        - **B** (Bedaquiline 100mg): 400 mg/d x 2 wk จากนั้น 200 mg/d (3 ครั้ง/wk)
        - **Pa** (Pretomanid 200mg): 200 mg/d
        - **L** (Linezolid 600mg): 600 mg/d (ลดเป็น 300 mg/d ได้ตามความทนยา)
        - **M** (Moxifloxacin 400mg): 400 mg/d
        - **Lfx** (Levofloxacin 750mg): 750-1,000 mg/d
        - **C** (Clofazimine 100mg): 100 mg/d
        - **E** (Ethambutol 400mg): 1,200-1,600 mg/d
        - **D** (Delamanid 50mg): <46kg 1 tab BD / >46kg 2 tab BD
        - **Z** (Pyrazinamide 500mg): 1,500-2,000 mg/d
        - **Eto/Pto** (250mg): <70kg 750mg / >70kg 1,000mg
        """)
        
    with tab_9m:
        st.markdown("""
        **ทางเลือกกรณีไม่ดื้อ Quinolones:**
        1. BLMZ
        2. BLLfxCZ
        3. BDLLfxZ
        4. DCLLfxZ
        5. DCMZ
        """)
        
    with tab_longer:
        st.markdown("""
        **สูตร 18 เดือนขึ้นไป:**
        - **Group A (เลือก 3):** Lfx/M, B, L
        - **Group B (เลือก 1-2):** C, Cs/Trd
        - **Group C (เลือกเพิ่มให้ครบ):** E, D, Z, Ipm-Cln/Mpm, Am, Pto/Eto, PAS
        """)

# 9. Minimal Disclaimer Footer
st.markdown("""
<div class="min-disclaimer">
    คำเตือน: เหมาะสำหรับผู้ประกอบวิชาชีพเวชกรรมเท่านั้น ผู้พัฒนาขอสงวนสิทธิ์ที่จะไม่รับผิดชอบต่อความเสียหายที่เกิดขึ้นจากการใช้โปรแกรมนี้<br>
    แหล่งข้อมูล: WHO Operational Handbook on Tuberculosis (Module 4, 2025) | มิถุนายน 2026
</div>
""", unsafe_allow_html=True)
