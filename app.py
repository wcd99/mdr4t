import streamlit as st

# 1. Page Configuration - Centered Mobile App Layout
st.set_page_config(
    page_title="MDR4T - MDR-TB Guide for Thai",
    page_icon="💊",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Sleek Dark Minimalist Styling (Bright High-Contrast Text Palette)
# Dark Base: #0F172A (Deep Slate Navy)
# Card Base: #1E293B (Dark Container)
# Accent Teal: #0F766E / #2DD4BF (Primary Highlight)
# Text High-Contrast: #FFFFFF (Pure White) & #E2E8F0 (Bright Light Silver)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Prompt:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', 'Prompt', -apple-system, BlinkMacSystemFont, sans-serif;
        background-color: #0f172a !important;
        color: #ffffff !important;
    }
    
    /* Hide Streamlit Chrome Elements */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    .stApp, .stAppViewContainer {
        background-color: #0f172a !important;
    }

    /* Force all text labels, paragraphs, spans to bright white */
    p, span, label, div, [class*="stMarkdown"], [class*="stCheckbox"], [class*="stRadio"] label {
        color: #ffffff !important;
    }
    
    /* Caption text styling - bright light silver */
    [data-testid="stCaptionContainer"], .stCaption {
        color: #e2e8f0 !important;
        font-size: 0.85rem !important;
    }

    /* Reduce Top Spacing for Mobile Screen */
    .main .block-container {
        max-width: 520px;
        padding-top: 0.3rem !important;
        padding-bottom: 1.5rem !important;
        padding-left: 0.8rem !important;
        padding-right: 0.8rem !important;
        margin: 0 auto;
    }
    
    /* Modern Compact Dark Mobile Header */
    .mobile-header {
        text-align: center;
        padding: 0.9rem 1rem 0.7rem 1rem;
        background-color: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        margin-bottom: 0.8rem;
    }
    
    .mobile-header h1 {
        font-size: 1.65rem;
        font-weight: 800;
        color: #ffffff !important;
        margin: 0;
        letter-spacing: -0.5px;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.4rem;
    }

    .mobile-header p {
        font-size: 0.85rem;
        color: #2dd4bf !important;
        font-weight: 600;
        margin-top: 0.15rem;
        margin-bottom: 0;
    }

    /* Dark Minimal Card Containers */
    .min-card {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 0.9rem 1.1rem;
        margin-bottom: 0.8rem;
        color: #ffffff;
    }

    .section-title {
        font-size: 0.95rem;
        font-weight: 800;
        color: #ffffff !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.5rem;
    }

    .min-badge {
        display: inline-block;
        padding: 0.35rem 0.85rem;
        border-radius: 6px;
        font-weight: 700;
        font-size: 0.98rem;
        background-color: #334155;
        color: #ffffff !important;
        border: 1px solid #475569;
    }

    .min-formula-box {
        background-color: #0f766e;
        color: #ffffff !important;
        padding: 0.9rem;
        border-radius: 8px;
        font-size: 1.4rem;
        font-weight: 800;
        text-align: center;
        letter-spacing: 0.5px;
        margin-top: 0.4rem;
        box-shadow: 0 4px 12px rgba(15, 118, 110, 0.4);
    }

    /* Input & Button Styling */
    .stTextInput input {
        background-color: #1e293b !important;
        color: #ffffff !important;
        border: 1px solid #334155 !important;
        border-radius: 8px !important;
    }
    .stButton > button {
        background-color: #0f766e !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        border-radius: 8px !important;
        border: none !important;
        transition: all 0.2s ease;
    }
    .stButton > button:hover {
        background-color: #14b8a6 !important;
        color: #ffffff !important;
    }
    .user-badge {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #1e293b;
        border: 1px solid #334155;
        border-radius: 10px;
        padding: 0.5rem 0.8rem;
        margin-bottom: 0.8rem;
        font-size: 0.85rem;
    }
</style>
""", unsafe_allow_html=True)

# 3. Minimal Mobile Header with Pill Icon 💊 (Dark Theme)
st.markdown("""
<div class="mobile-header">
    <h1>💊 MDR4T</h1>
    <p>โปรแกรมช่วยเลือกสูตรการรักษาวัณโรคปอดดื้อยา</p>
</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# กำหนดรหัสลับเฉพาะกลุ่ม (Access Codes & Authorized Groups)
# ----------------------------------------------------
# ท่านสามารถเพิ่ม/แก้ไข/ลบ รหัสผ่านและกลุ่มผู้ใช้งานได้ที่นี่
ACCESS_CODES = {
    "MDR4SI": "แพทย์และบุคลากรทางการแพทย์ (Medical Staff)",
    "SI2025": "กลุ่มโรงพยาบาลศิริราช (Siriraj TB Team)",
    "TB2025": "ทีมควบคุมวัณโรค (TB Control Unit)",
    "EXPERT": "ผู้เชี่ยวชาญวัณโรคดื้อยา (TB Specialist)",
    "DEMO": "ผู้ทดสอบระบบ (Trial / Guest)"
}

# รองรับการดึงรหัสเพิ่มเติมจาก Streamlit Secrets (.streamlit/secrets.toml) หากมี
if "ACCESS_CODES" in st.secrets:
    try:
        ACCESS_CODES.update(dict(st.secrets["ACCESS_CODES"]))
    except Exception:
        pass

# จัดการสถานะการยืนยันตัวตนใน Session State
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.user_group = ""
    st.session_state.user_code = ""

# ส่วนกรองผู้ใช้งาน (Access Gatekeeper)
if not st.session_state.authenticated:
    st.markdown("""
    <div class="min-card" style="text-align: center; margin-top: 0.5rem; padding: 1.2rem 1rem;">
        <div style="font-size: 2.2rem; margin-bottom: 0.4rem;">🔒</div>
        <div class="section-title" style="margin-bottom: 0.3rem;">ยืนยันสิทธิ์การเข้าใช้งาน</div>
        <p style="font-size: 0.85rem; color: #94a3b8; margin-bottom: 0.2rem;">
            ระบบนี้สงวนสิทธิ์เฉพาะกลุ่มผู้ได้รับอนุญาตเท่านั้น
        </p>
        <p style="font-size: 0.78rem; color: #64748b; margin-bottom: 0.8rem;">
            โปรดระบุ Code ลับเฉพาะกลุ่มของท่านเพื่อเข้าสู่ระบบ
        </p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("access_verification_form", clear_on_submit=False):
        code_input = st.text_input(
            "🔑 รหัสเข้าใช้งาน (Access Code)",
            type="password",
            placeholder="กรอกรหัสลับเฉพาะกลุ่ม..."
        )
        submit_btn = st.form_submit_button("เข้าสู่ระบบ 🚀", use_container_width=True)

        if submit_btn:
            cleaned_code = code_input.strip().upper()
            matched_group = None
            
            # ค้นหารหัสที่ตรงกัน (Case-insensitive)
            for valid_code, group_name in ACCESS_CODES.items():
                if cleaned_code == valid_code.upper():
                    matched_group = group_name
                    break
            
            if matched_group:
                st.session_state.authenticated = True
                st.session_state.user_group = matched_group
                st.session_state.user_code = cleaned_code
                st.success("✅ ยืนยันสิทธิ์สำเร็จ กำลังเข้าสู่ระบบ...")
                st.rerun()
            else:
                st.error("❌ รหัสลับไม่ถูกต้อง หรือท่านไม่มีสิทธิ์เข้าใช้งาน")

    st.markdown("""
    <div class="min-disclaimer">
        คำเตือน: เหมาะสำหรับผู้ประกอบวิชาชีพเวชกรรมและกลุ่มผู้มีสิทธิ์เข้าถึงเท่านั้น<br>
        หากต้องการรหัสเข้าใช้งาน กรุณาติดต่อผู้ดูแลระบบ
    </div>
    """, unsafe_allow_html=True)
    
    st.stop()  # หยุดการทำงานหากยังไม่ผ่านการยืนยันรหัสผ่าน

# แสดงแถบข้อมูลกลุ่มผู้ใช้งานเมื่อผ่านการตรวจสอบแล้ว พร้อมปุ่มออกจากระบบ
col_user, col_logout = st.columns([3, 1])
with col_user:
    st.markdown(f"""
    <div style="font-size: 0.85rem; color: #2dd4bf; padding-top: 0.4rem; font-weight: 600;">
        👤 กลุ่ม: <span style="color: #ffffff;">{st.session_state.user_group}</span>
    </div>
    """, unsafe_allow_html=True)
with col_logout:
    if st.button("🚪 ออก", use_container_width=True, help="ออกจากระบบ"):
        st.session_state.authenticated = False
        st.session_state.user_group = ""
        st.session_state.user_code = ""
        st.rerun()

st.markdown("<div style='margin-bottom: 0.5rem;'></div>", unsafe_allow_html=True)

# 4. Logic Functions
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

# 5. Form Inputs
with st.container():
    st.markdown('<div class="section-title">1. การดื้อยา</div>', unsafe_allow_html=True)
    with st.container(border=True):
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
    <div style="font-size: 0.82rem; color: #e2e8f0; margin-bottom: 0.3rem; font-weight: 500;">รูปแบบการดื้อยา</div>
    <div class="min-badge">{pattern_text}</div>
    <div style="font-size: 0.82rem; color: #e2e8f0; margin-top: 0.8rem; margin-bottom: 0.2rem; font-weight: 500;">สูตรยาที่แนะนำ</div>
    <div class="min-formula-box">{recommended_formula}</div>
</div>
""", unsafe_allow_html=True)


# 8. Reference Dosing & Drug Groups
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
    แหล่งข้อมูล: WHO Operational Handbook on Tuberculosis (Module 4, 2025)
</div>
""", unsafe_allow_html=True)
