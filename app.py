import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="MDR4T - MDR-TB Guide for Thai",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Modern Custom Styling (CSS)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Prompt', 'Inter', sans-serif;
    }
    
    /* Header Gradient & Hero Section */
    .hero-container {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f766e 100%);
        padding: 1.8rem 2rem;
        border-radius: 16px;
        color: white;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.2);
        margin-bottom: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .hero-title {
        font-size: 2.2rem;
        font-weight: 700;
        margin: 0;
        background: linear-gradient(90deg, #38bdf8, #2dd4bf);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .hero-subtitle {
        font-size: 1.05rem;
        color: #94a3b8;
        margin-top: 0.4rem;
        margin-bottom: 0;
    }

    .badge-year {
        background: rgba(45, 212, 191, 0.15);
        color: #2dd4bf;
        border: 1px solid rgba(45, 212, 191, 0.3);
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
    }

    /* Result Card Styles */
    .result-card {
        background: #ffffff;
        border-radius: 14px;
        padding: 1.5rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
        border: 1px solid #e2e8f0;
        margin-bottom: 1.2rem;
    }

    @media (prefers-color-scheme: dark) {
        .result-card {
            background: #1e293b;
            border-color: #334155;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        }
    }

    .pattern-badge {
        display: inline-block;
        padding: 0.5rem 1.2rem;
        border-radius: 30px;
        font-weight: 700;
        font-size: 1.15rem;
        letter-spacing: 0.5px;
    }

    .badge-hr { background-color: #fef3c7; color: #92400e; border: 1px solid #fcd34d; }
    .badge-rr { background-color: #e0f2fe; color: #075985; border: 1px solid #bae6fd; }
    .badge-mdr { background-color: #ffedd5; color: #c2410c; border: 1px solid #fed7aa; }
    .badge-prexdr { background-color: #fce7f3; color: #be185d; border: 1px solid #fbcfe8; }
    .badge-xdr { background-color: #fee2e2; color: #991b1b; border: 1px solid #fca5a5; }
    .badge-none { background-color: #f1f5f9; color: #475569; border: 1px solid #cbd5e1; }

    .formula-box {
        background: linear-gradient(135deg, #0284c7 0%, #0d9488 100%);
        color: white;
        padding: 1.25rem 1.5rem;
        border-radius: 12px;
        font-size: 1.75rem;
        font-weight: 700;
        text-align: center;
        letter-spacing: 1px;
        box-shadow: 0 6px 15px rgba(13, 148, 136, 0.25);
        margin: 0.8rem 0;
    }

    .drug-chip {
        display: inline-block;
        background: #0f766e;
        color: #ffffff;
        padding: 0.2rem 0.6rem;
        border-radius: 6px;
        font-size: 0.85rem;
        font-weight: 700;
        margin-right: 0.4rem;
    }

    .summary-box {
        background: #f8fafc;
        border: 1px dashed #94a3b8;
        border-radius: 8px;
        padding: 1rem;
        font-family: monospace;
        font-size: 0.88rem;
        color: #334155;
    }

    @media (prefers-color-scheme: dark) {
        .summary-box {
            background: #0f172a;
            border-color: #475569;
            color: #cbd5e1;
        }
    }

    .disclaimer-box {
        background-color: rgba(245, 158, 11, 0.1);
        border-left: 4px solid #f59e0b;
        padding: 1rem 1.2rem;
        border-radius: 8px;
        color: #b45309;
        font-size: 0.88rem;
        margin-top: 2rem;
    }

    @media (prefers-color-scheme: dark) {
        .disclaimer-box {
            background-color: rgba(245, 158, 11, 0.15);
            color: #fcd34d;
        }
    }
</style>
""", unsafe_allow_html=True)

# 3. Header UI
st.markdown("""
<div class="hero-container">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap:1rem;">
        <div>
            <h1 class="hero-title">🩺 MDR4T <span style="font-size:1.2rem; font-weight:400; color:#38bdf8;">| MDR-TB Guide for Thai</span></h1>
            <p class="hero-subtitle">โปรแกรมช่วยเลือกสูตรการรักษาวัณโรคปอดดื้อยา (Drug-Resistant Pulmonary TB Regimen Selector)</p>
        </div>
        <div>
            <span class="badge-year">WHO Handbook 2025 Standard</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 4. Logic Functions
def calculate_resistance_pattern(H, R, Q, A):
    if H and not R:
        return "Rifampicin-susceptible, INH-resistant (Hr-TB)", "badge-hr"
    elif not H and R:
        if Q == "not resist":
            return "RR-TB", "badge-rr"
        elif Q == "not known":
            return "RR-TB, FQ susceptibility pending", "badge-rr"
        elif Q == "resist":
            if not A:
                return "Pre-XDR-TB", "badge-prexdr"
            else:
                return "XDR-TB", "badge-xdr"
    elif H and R:
        if Q == "not resist":
            return "MDR-TB", "badge-mdr"
        elif Q == "not known":
            return "MDR-TB, FQ susceptibility pending", "badge-mdr"
        elif Q == "resist":
            if not A:
                return "Pre-XDR-TB", "badge-prexdr"
            else:
                return "XDR-TB", "badge-xdr"
    elif R and Q == "resist":
        if not A:
            return "Pre-XDR-TB", "badge-prexdr"
        else:
            return "XDR-TB", "badge-xdr"
    else:
        return "ไม่พบรูปแบบดื้อยาเฉพาะ (Drug Susceptible / Pending)", "badge-none"

def calculate_recommended_formula(H, R, Q, A, kid, pregnant):
    # INH Resistance alone
    if H and not R:
        if Q in ["not resist", "not known"]:
            return "6REZLfx หรือ 6(H)REZLfx (กรณีเป็นยาผสม)"
        elif Q == "resist":
            return "6REZ หรือ 6(H)REZ (กรณีเป็นยาผสม)"
    
    # MDR/RR
    elif R:
        if Q == "resist":
            if A:
                return "Longer 18-m regimen"
            else:
                if kid or pregnant:
                    return "6BDLC"
                else:
                    return "6BPAL"
        else:  # Q in ["not resist", "not known"]
            if kid or pregnant:
                return "6BDLLfx"
            else:
                return "6BPaLM"
                
    return "โปรดระบุการดื้อยา H หรือ R เพื่อประเมินสูตรยา"

# 5. Main Layout Columns
col_inputs, col_results = st.columns([1, 1.1], gap="large")

with col_inputs:
    st.markdown("### 🧪 1. ประวัติการดื้อยา (Drug Resistance Profile)")
    
    with st.container(border=True):
        st.markdown("**ผลความไวต่อยาต้านวัณโรค (Drug Susceptibility Testing):**")
        
        c1, c2 = st.columns(2)
        with c1:
            h_resist = st.checkbox("Isoniazid (H)", value=False, help="ดื้อยา Isoniazid")
        with c2:
            r_resist = st.checkbox("Rifampicin (R)", value=False, help="ดื้อยา Rifampicin")
        
        st.markdown("---")
        st.markdown("**Fluoroquinolone (FQ):**")
        fq_status = st.radio(
            "สถานะความไวต่อยา FQ",
            options=["not known", "not resist", "resist"],
            format_func=lambda x: {
                "not known": "❓ ไม่ทราบผล / รอผล (Not known)",
                "not resist": "✅ ไม่ดื้อยา (Not resist / Susceptible)",
                "resist": "⚠️ ดื้อยา (Resist)"
            }[x],
            index=0,
            label_visibility="collapsed"
        )
        
        group_a_resist = False
        if fq_status == "resist":
            st.markdown("---")
            st.warning("⚠️ กรณีดื้อยา Fluoroquinolone (FQ)")
            group_a_resist = st.checkbox(
                "ดื้อยา Group A เพิ่มเติม (Bedaquiline หรือ Linezolid)",
                value=False,
                help="เลือกหากพบการดื้อยา Bedaquiline หรือ Linezolid ร่วมด้วย"
            )

    st.markdown("### 👤 2. ลักษณะผู้ป่วย (Patient Characteristics)")
    with st.container(border=True):
        is_kid = st.checkbox("👶 อายุน้อยกว่า 14 ปี (< 14 years old)", value=False)
        is_pregnant = st.checkbox("🤰 ตั้งครรภ์ หรือ ให้นมบุตร (Pregnant / Lactating)", value=False)

# Perform Calculations
pattern_text, pattern_badge_class = calculate_resistance_pattern(h_resist, r_resist, fq_status, group_a_resist)
recommended_formula = calculate_recommended_formula(h_resist, r_resist, fq_status, group_a_resist, is_kid, is_pregnant)

# 6. Results Column
with col_results:
    st.markdown("### 📊 3. ผลการวิเคราะห์และสูตรยาแนะนำ")
    
    # Pattern Card
    st.markdown(f"""
    <div class="result-card">
        <div style="font-size: 0.88rem; color: #64748b; font-weight:600; text-transform: uppercase; margin-bottom:0.5rem;">
            🧬 รูปแบบการดื้อยา (Drug Resistance Pattern)
        </div>
        <div class="pattern-badge {pattern_badge_class}">
            {pattern_text}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Formula Card
    st.markdown(f"""
    <div class="result-card" style="border-top: 4px solid #0d9488;">
        <div style="font-size: 0.88rem; color: #64748b; font-weight:600; text-transform: uppercase; margin-bottom:0.5rem;">
            💊 สูตรยาที่แนะนำ (Recommended Regimen)
        </div>
        <div class="formula-box">
            {recommended_formula}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Formula Breakdown details
    with st.expander("🔍 คำอธิบายรหัสสูตรยาและส่วนประกอบ (Regimen Breakdown)", expanded=True):
        if "6BPaLM" in recommended_formula:
            st.markdown("""
            **6BPaLM**: สูตรระยะสั้น 6 เดือน ประกอบด้วย
            - **B**edaquiline + **Pa**retomanid + **L**inezolid + **M**oxifloxacin
            - *เป็นสูตรหลักที่แนะนำสำหรับผู้ใหญ่ที่ไม่ดื้อ FQ และไม่ตั้งครรภ์*
            """)
        elif "6BPAL" in recommended_formula:
            st.markdown("""
            **6BPAL**: สูตรระยะสั้น 6 เดือน สำหรับ Pre-XDR TB ประกอบด้วย
            - **B**edaquiline + **Pa**retomanid + **L**inezolid
            """)
        elif "6BDLLfx" in recommended_formula:
            st.markdown("""
            **6BDLLfx**: สูตรสำหรับเด็ก (<14 ปี) หรือ สตรีตั้งครรภ์/ให้นมบุตร ประกอบด้วย
            - **B**edaquiline + **D**elamanid + **L**inezolid + **Lfx** (Levofloxacin)
            """)
        elif "6BDLC" in recommended_formula:
            st.markdown("""
            **6BDLC**: สูตรสำหรับเด็ก (<14 ปี) หรือ สตรีตั้งครรภ์/ให้นมบุตร ที่ดื้อ FQ ประกอบด้วย
            - **B**edaquiline + **D**elamanid + **L**inezolid + **C**lofazimine
            """)
        elif "6REZLfx" in recommended_formula or "6REZ" in recommended_formula:
            st.markdown("""
            **6REZLfx / 6REZ**: สูตรสำหรับ Hr-TB (ดื้อเฉพาะ INH)
            - R: Rifampicin, E: Ethambutol, Z: Pyrazinamide, Lfx: Levofloxacin
            """)
        elif "Longer" in recommended_formula:
            st.markdown("""
            **Longer 18-m regimen**: สูตรยารักษาระยะยาว (18 เดือนขึ้นไป)
            - ออกแบบสูตรยาเฉพาะรายบุคคล โดยเลือกยากลุ่ม A (3 ตัว) + กลุ่ม B (1-2 ตัว) + กลุ่ม C ตามข้อบ่งชี้
            """)
        else:
            st.info("ระบุข้อมูลการดื้อยาด้านซ้าย เพื่อดูคำอธิบายรายละเอียดสูตรยา")

    # Clinical Note Copy Generator
    with st.expander("📋 สรุปผลสำหรับการบันทึกเวชระเบียน (Clinical Note Summary)"):
        fq_th = {"not known": "ไม่ทราบผล/รอผล", "not resist": "ไม่ดื้อยา", "resist": "ดื้อยา"}[fq_status]
        summary_text = (
            f"MDR4T Clinical Decision Support Summary\n"
            f"----------------------------------------\n"
            f"• Resistance DST: H={h_resist}, R={r_resist}, FQ={fq_th}"
            + (f", Group A Resist={group_a_resist}" if fq_status == "resist" else "") + "\n"
            f"• Patient Profile: Child (<14y)={is_kid}, Pregnant/Lactating={is_pregnant}\n"
            f"• Resistance Pattern: {pattern_text}\n"
            f"• Recommended Regimen: {recommended_formula}\n"
            f"----------------------------------------\n"
            f"Ref: WHO Operational Handbook on TB (Module 4, 2025)"
        )
        st.code(summary_text, language="text")

st.markdown("---")

# 7. Interactive Dose & Drug Reference Section
st.markdown("### 📚 ข้อมูลขนาดยา และกลุ่มยาอ้างอิง")

# Control option to toggle reference details
see_details = st.radio(
    "แสดงข้อมูลขนาดยาและกลุ่มยาอ้างอิง (View Dosing & Drug Groups)",
    options=["แสดง (Yes)", "ซ่อน (No)"],
    horizontal=True,
    index=0
)

if see_details == "แสดง (Yes)":
    tab_dose, tab_9m, tab_longer = st.tabs([
        "💊 ขนาดยาผู้ใหญ่ (Adult Dosages)", 
        "⏱️ กลุ่มยาสำหรับ 9-Month Regimens", 
        "🧬 กลุ่มยาสำหรับ Longer Regimens"
    ])

    with tab_dose:
        st.markdown("#### ขนาดยาสำหรับผู้ใหญ่ (Adult Dosing)")
        dosages = [
            {"code": "B", "name": "Bedaquiline", "strength": "100 mg", "dose": "400 mg/day เป็นเวลา 2 สัปดาห์ จากนั้น 200 mg/day สัปดาห์ละ 3 ครั้ง (หรือ 200 mg/day 8 สัปดาห์ จากนั้น 100 mg/day)"},
            {"code": "Pa", "name": "Pretomanid", "strength": "200 mg", "dose": "200 mg/day"},
            {"code": "L", "name": "Linezolid", "strength": "600 mg", "dose": "600 mg/day (สามารถลดขนาดเหลือ 300 mg/day ตามความทนต่อยาของผู้ป่วย)"},
            {"code": "M", "name": "Moxifloxacin", "strength": "400 mg", "dose": "400 mg/day"},
            {"code": "Lfx", "name": "Levofloxacin", "strength": "750 mg", "dose": "750 - 1,000 mg/day"},
            {"code": "C", "name": "Clofazimine", "strength": "100 mg", "dose": "100 mg/day"},
            {"code": "E", "name": "Ethambutol", "strength": "400 mg", "dose": "1,200 - 1,600 mg/day"},
            {"code": "D", "name": "Delamanid", "strength": "50 mg", "dose": "1 เม็ด BD (น้ำหนัก < 46 kg) / 2 เม็ด BD (น้ำหนัก > 46 kg)"},
            {"code": "Z", "name": "Pyrazinamide", "strength": "500 mg", "dose": "1,500 - 2,000 mg/day"},
            {"code": "Eto/Pto", "name": "Ethionamide / Protionamide", "strength": "250 mg", "dose": "750 mg/day (น้ำหนัก < 70 kg) / 1,000 mg/day (น้ำหนัก > 70 kg)"}
        ]
        
        for item in dosages:
            col_code, col_detail = st.columns([1.2, 3.8])
            with col_code:
                st.markdown(f"<span class='drug-chip'>{item['code']}</span> <strong>{item['name']}</strong> ({item['strength']})", unsafe_allow_html=True)
            with col_detail:
                st.markdown(f"👉 {item['dose']}")

    with tab_9m:
        st.markdown("#### กลุ่มยาสำหรับ 9-Month Regimens")
        st.caption("ใช้เป็นทางเลือกในกรณีที่ไม่ดื้อต่อยา Quinolones (Fluoroquinolones)")
        
        regimens_9m = ["BLMZ", "BLLfxCZ", "BDLLfxZ", "DCLLfxZ", "DCMZ"]
        cols = st.columns(5)
        for i, reg in enumerate(regimens_9m):
            with cols[i]:
                st.markdown(f"""
                <div style="background: #f8fafc; border:1px solid #cbd5e1; border-radius:10px; padding:1rem 0.5rem; text-align:center; margin-bottom:0.8rem; font-weight:700; color:#0f766e; font-size:1.15rem;">
                    🧪 {reg}
                </div>
                """, unsafe_allow_html=True)

    with tab_longer:
        st.markdown("#### กลุ่มยาสำหรับ Longer Regimens (18-20 เดือน)")
        
        c_ga, c_gb, c_gc = st.columns(3)
        
        with c_ga:
            st.markdown("""
            <div style="background:#eff6ff; border:1px solid #bfdbfe; border-radius:10px; padding:1rem; height:100%;">
                <h5 style="color:#1d4ed8; margin-top:0;">Group A (เลือก 3 ขนาน)</h5>
                <ul style="padding-left:1.2rem; font-size:0.9rem;">
                    <li><strong>Lfx</strong>: Levofloxacin / <strong>M</strong>: Moxifloxacin</li>
                    <li><strong>B</strong>: Bedaquiline</li>
                    <li><strong>L</strong>: Linezolid</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
        with c_gb:
            st.markdown("""
            <div style="background:#f0fdf4; border:1px solid #bbf7d0; border-radius:10px; padding:1rem; height:100%;">
                <h5 style="color:#15803d; margin-top:0;">Group B (เลือกเพิ่ม 1-2 ขนาน)</h5>
                <ul style="padding-left:1.2rem; font-size:0.9rem;">
                    <li><strong>C</strong>: Clofazimine</li>
                    <li><strong>Cs/Trd</strong>: Cycloserine / Terizidone</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
        with c_gc:
            st.markdown("""
            <div style="background:#fefce8; border:1px solid #fef08a; border-radius:10px; padding:1rem; height:100%;">
                <h5 style="color:#a16207; margin-top:0;">Group C (เลือกเพิ่มให้ครบ หรือ เมื่อไม่สามารถใช้กลุ่ม A, B)</h5>
                <ul style="padding-left:1.2rem; font-size:0.85rem;">
                    <li><strong>E</strong>: Ethambutol, <strong>D</strong>: Delamanid, <strong>Z</strong>: Pyrazinamide</li>
                    <li><strong>Ipm-Cln</strong>: Imipenem-cilastatin / <strong>Mpm</strong>: Meropenem</li>
                    <li><strong>Am</strong>: Amikacin</li>
                    <li><strong>Pto/Eto</strong>: Protionamide / Ethionamide</li>
                    <li><strong>PAS</strong>: p-aminosalicylic acid</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

# 8. Footer & Medical Disclaimer
st.markdown("""
<div class="disclaimer-box">
    <strong>⚠️ คำเตือน:</strong> เหมาะสำหรับผู้ประกอบวิชาชีพเวชกรรมเท่านั้น ผู้พัฒนาขอสงวนสิทธิ์ที่จะไม่รับผิดชอบต่อความเสียหายที่เกิดขึ้นจากการใช้โปรแกรมนี้
    <br><br>
    📖 <strong>แหล่งข้อมูล:</strong> WHO Operational Handbook on Tuberculosis: Module 4: Treatment and Care (2025)
    <br>
    📅 <strong>เวอร์ชัน:</strong> มิถุนายน 2026 (June 2026)
</div>
""", unsafe_allow_html=True)
