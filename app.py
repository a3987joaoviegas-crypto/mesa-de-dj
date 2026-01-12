if 'neon_color' not in st.session_state:
    st.session_state.neon_color = "#00ff00"import streamlit as st
import streamlit.components.v1 as components
import time

st.set_page_config(page_title="DJ MASTER MIXER - NEON EDITION", layout="wide", page_icon="🎧")

# --- ESTILO VISUAL MESA DE DJ com NEONS e ANIMAÇÕES ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap');
    
    .stApp {{ background-color: #000000; color: #00ff00; font-family: 'Orbitron', sans-serif; }}
    
    .dj-plate {{
        border: 8px solid #333;
        border-radius: 50%;
        width: 250px;
        height: 250px;
        background: radial-gradient(circle, #111 40%, #222 50%, #000 100%);
        margin: auto;
        box-shadow: 0 0 20px rgba(0,255,0,0.5); /* Neon glow */
        position: relative;
        overflow: hidden;
    }}
    .dj-plate::before {{
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        border-radius: 50%;
        border: 5px dashed #00ff00; /* Linha de rotação */
        animation: rotatePlate 5s linear infinite;
        animation-play-state: paused; /* Inicia pausada */
    }}
    .dj-plate.playing::before {{
        animation-play-state: running; /* Roda quando 'playing' */
    }}
    @keyframes rotatePlate {{ from {{ transform: rotate(0deg); }} to {{ transform: rotate(360deg); }} }}

    .control-panel {{ background: #1a1a1a; padding: 20px; border-radius: 15px; border: 2px solid #444; }}
    
    /* NEON LIGHTS PANEL */
    .neon-panel {{
        background: linear-gradient(to right, #111 1%, #000 50%, #111 99%);
        border: 2px solid #00ff00;
        border-radius: 10px;
        padding: 10px 0;
        margin-top: 30px;
        display: flex;
        justify-content: space-around;
        align-items: center;
    }}
    .neon-light {{
        width: 30px; height: 30px; border-radius: 50%;
        background-color: #00ff00; /* Cor padrão */
        box-shadow: 0 0 10px #00ff00, 0 0 20px #00ff00, 0 0 30px #00ff00;
        transition: all 0.1s ease-in-out;
    }}
    .neon-light.active {{
        background-color: {st.session_state.neon_color}; /* Cor selecionada */
        box-shadow: 0 0 15px {st.session_state.neon_color}, 0 0 30px {st.session_state.neon_color}, 0 0 45px {st.session_state.neon_color};
    }}
    .stSlider > div > div > div:nth-child(1) {{ background-color: #00ff00; }} /* Cor do slider */
    .stButton>button {{ background-color: #00ff00; color: black; border-radius: 5px; }}
    </style>
    """, unsafe_allow_html=True)

# Inicializar estados para a cor do neon e estado das placas
if 'neon_color' not in st.session_state:
    st.session_state.neon_color = "#00ff00"
if 'plateA_playing' not in st.session_state:
    st.session_state.plateA_playing = False
if 'plateB_playing' not in st.session_state:
    st.session_state.plateB_playing = False

# Função para acender uma luz de neon (simulação)
def activate_neon_light(light_id):
    st.session_state[f'neon_active_{light_id}'] = True
    time.sleep(0.1) # Breve pausa para o efeito visual
    st.session_state[f'neon_active_{light_id}'] = False

# --- TÍTULO PRINCIPAL ---
st.title("🎧 DJ PRO STUDIO - NEON EDITION")

# --- PAINEL DE NEONS ---
st.markdown("<h2 style='text-align: center; color: #00ff00;'>⚡ NEON LIGHT SHOW ⚡</h2>", unsafe_allow_html=True)
neon_cols = st.columns(5)
for i in range(5):
    neon_class = "neon-light active" if st.session_state.get(f'neon_active_{i}', False) else "neon-light"
    with neon_cols[i]:
        st.markdown(f'<div class="{neon_class}"></div>', unsafe_allow_html=True)

st.divider()

# --- COLUNAS PRINCIPAIS (Pratos de DJ) ---
col1, col2, col3 = st.columns([2, 1, 2])

with col1:
    st.subheader("DECK A")
    plate_class_a = "dj-plate playing" if st.session_state.plateA_playing else "dj-plate"
    st.markdown(f'<div class="{plate_class_a}" id="plateA"></div>', unsafe_allow_html=True)
    st.slider("Pitch Control A", -10.0, 10.0, 0.0, key="pitchA", help="Altera a velocidade da música.")
    if st.button("PLAY / PAUSE A", use_container_width=True, key="btnPlayA"):
        st.session_state.plateA_playing = not st.session_state.plateA_playing
        activate_neon_light(0) # Acende uma luz

with col2:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.write("🎚️ MIXER CENTRAL")
    st.slider("CROSSFADER", -100, 100, 0, help="Mistura o som entre o Deck A e o Deck B.")
    if st.button("⚡ EFFECT: AIRHORN", use_container_width=True, key="btnAirhorn"):
        activate_neon_light(1)
    if st.button("🥁 BEAT: KICK", use_container_width=True, key="btnKick"):
        activate_neon_light(2)

with col3:
    st.subheader("DECK B")
    plate_class_b = "dj-plate playing" if st.session_state.plateB_playing else "dj-plate"
    st.markdown(f'<div class="{plate_class_b}" id="plateB"></div>', unsafe_allow_html=True)
    st.slider("Pitch Control B", -10.0, 10.0, 0.0, key="pitchB", help="Altera a velocidade da música.")
    if st.button("PLAY / PAUSE B", use_container_width=True, key="btnPlayB"):
        st.session_state.plateB_playing = not st.session_state.plateB_playing
        activate_neon_light(3) # Acende outra luz

st.divider()

# --- NAVEGADOR SPOTIFY E INSTRUMENTOS ---
tab1, tab2, tab3 = st.tabs(["🎵 Spotify Browser", "🎸 Instrumentos MIDI", "📝 Playlist & Remix"])

with tab1:
    st.write("### Carregar Música do Spotify")
    st.info("Copia o URL de uma faixa do Spotify e cola aqui para carregar o player. (Ex: https://open.spotify.com/track/...)")
    song_link = st.text_input("URL da Música Spotify:", "https://open.spotify.com/track/4WpXW508v9gJ5rUvR238xL?si=2e1a3c7a23c84d7a", help="Cole o link da música aqui.")
    
    if "track/" in song_link:
        track_id = song_link.split("track/")[1].split("?")[0]
        embed_url = f"https://open.spotify.com/embed/track/{track_id}"
        components.html(f'<iframe src="{embed_url}" width="100%" height="352" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>', height=352)
    else:
        st.warning("Por favor, insere um URL válido de uma faixa do Spotify.")


with tab2:
    st.write("### 🎹 Banco de Instrumentos & Samples")
    st.info("Em desenvolvimento: Em breve poderás tocar instrumentos virtuais aqui!")
    inst_col1, inst_col2, inst_col3 = st.columns(3)
    with inst_col1:
        if st.button("🎹 Piano C4", key="pianoC4"): activate_neon_light(4)
        if st.button("🎹 Piano E4", key="pianoE4"): activate_neon_light(0)
    with inst_col2:
        if st.button("🎸 Guitar Chord", key="guitarCh"): activate_neon_light(1)
        if st.button("🎸 Bass Note", key="bassNote"): activate_neon_light(2)
    with inst_col3:
        if st.button("🎺 Trumpet", key="trumpet"): activate_neon_light(3)
        if st.button("🎻 Violin", key="violin"): activate_neon_light(4)
    
    st.slider("Volume Master", 0, 100, 80, help="Controla o volume geral dos instrumentos.")

with tab3:
    st.write("### 🎼 Linha de Produção & Remixes")
    st.text_area("Notas do Remix / Ordem das Músicas", "1. Intro - Batida\n2. Transição Deck A -> B\n3. Solo de Piano e Synth", height=200)
    st.multiselect("Adicionar Efeitos à Linha", ["Reverb", "Echo", "Distortion", "Flanger", "Phaser"], help="Aplica efeitos às faixas na tua linha de tempo.")
    st.button("GRAVAR REMIX", use_container_width=True, help="Grava a tua mixagem (funcionalidade futura).")

# --- RODAPÉ/SETTINGS ---
st.sidebar.title("🛠️ DJ SETTINGS")
st.session_state.neon_color = st.sidebar.color_picker("Cor dos Neons", st.session_state.neon_color)
st.sidebar.checkbox("Sync Decks (Funcionalidade Futura)", help="Sincroniza automaticamente o BPM dos dois decks.")
st.sidebar.info("A tua consola de DJ está pronta para agitar a pista! Explora os controlos e cria as tuas mixagens.")

# JavaScript para atualizar as placas (Streamlit não executa diretamente JS)
# Isto é uma simulação visual
if st.session_state.plateA_playing:
    components.html("<script>document.getElementById('plateA').classList.add('playing');</script>", height=0)
else:
    components.html("<script>document.getElementById('plateA').classList.remove('playing');</script>", height=0)

if st.session_state.plateB_playing:
    components.html("<script>document.getElementById('plateB').classList.add('playing');</script>", height=0)
else:
    components.html("<script>document.getElementById('plateB').classList.remove('playing');</script>", height=0)
