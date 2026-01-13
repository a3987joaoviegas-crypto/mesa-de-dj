import streamlit as st
import base64 # Para ícones e imagens embutidas (se necessário)

# --- Configuração da Página ---
st.set_page_config(
    layout="wide",
    page_title="Gemini Digital DJ Deck - SoundCloud Edition",
    initial_sidebar_state="expanded"
)

# --- CSS para Estilização "Ultra Realista" e Layout da Imagem ---
st.markdown("""
<style>
    /* Estilo geral da página */
    .main {
        background-color: #1a1a1e; /* Fundo cinza escuro para simular a imagem */
        color: #e0e0e0; /* Cor do texto padrão */
        font-family: 'Inter', sans-serif; /* Fonte moderna */
    }
    .st-emotion-cache-z5fcl4 { /* Sidebar container */
        background-color: #2b2b30; /* Fundo da sidebar */
        border-right: 1px solid #3a3a3f;
    }
    .st-emotion-cache-1pxazr7 { /* Sidebar title (Music Browser) */
        color: #ffffff;
    }

    /* Layout principal com 3 colunas para simular a imagem */
    .reportview-container .main .block-container {
        padding-top: 1rem;
        padding-right: 1rem;
        padding-left: 1rem;
        padding-bottom: 1rem;
    }

    /* Contêiner principal da aplicação (imitando a moldura da janela) */
    .app-frame {
        background-color: #2b2b30; /* Cor da moldura */
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
        padding: 10px;
        margin-bottom: 20px;
        display: flex;
        flex-direction: column;
        height: 85vh; /* Ajusta a altura da janela */
    }

    /* Barra de título da janela (simulada) */
    .window-title-bar {
        background-color: #2b2b30;
        padding: 8px 15px;
        border-top-left-radius: 10px;
        border-top-right-radius: 10px;
        display: flex;
        align-items: center;
        gap: 8px;
        color: #ccc;
        font-size: 0.9em;
        position: sticky; /* Mantém a barra de título no topo */
        top: 0;
        z-index: 10;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    .window-title-bar .traffic-lights {
        display: flex;
        gap: 6px;
    }
    .window-title-bar .traffic-light {
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background-color: #ccc; /* Cor neutra para as bolinhas */
    }
    .window-title-bar .traffic-light.red { background-color: #ff605c; }
    .window-title-bar .traffic-light.yellow { background-color: #ffbd44; }
    .window-title-bar .traffic-light.green { background-color: #00ca4e; }
    .window-title-bar .app-name {
        flex-grow: 1;
        text-align: center;
        font-weight: bold;
        color: #fff;
    }

    /* Layout interno da aplicação */
    .app-content {
        display: flex;
        flex-grow: 1; /* Permite que o conteúdo ocupe o espaço restante */
        overflow: hidden; /* Para lidar com conteúdo rolante nas colunas */
    }

    /* Coluna do navegador esquerdo (SoundCloud) */
    .left-browser-col {
        width: 250px; /* Largura fixa como na imagem */
        background-color: #242428; /* Fundo mais escuro */
        padding: 15px;
        border-right: 1px solid #3a3a3f;
        border-bottom-left-radius: 10px;
        overflow-y: auto; /* Rolagem para o conteúdo */
        flex-shrink: 0; /* Não encolher */
    }

    /* Coluna central da mesa de DJ */
    .dj-deck-col {
        flex-grow: 1; /* Ocupa o espaço restante */
        padding: 15px;
        background-color: #1a1a1e; /* Fundo principal da mesa */
        display: flex;
        flex-direction: column;
    }

    /* O retangulo preto da mesa de DJ */
    .dj-table-placeholder {
        background-color: #0d0d0f; /* Preto muito escuro */
        border-radius: 8px;
        padding: 20px;
        flex-grow: 1; /* Ocupa o espaço disponível */
        display: flex;
        flex-direction: column;
        justify-content: center; /* Centraliza verticalmente o conteúdo (se houver) */
        align-items: center; /* Centraliza horizontalmente o conteúdo */
        border: 1px solid #2a2a2e;
        position: relative; /* Para posicionar o mixer dentro */
    }

    /* Estilo para os discos de vinil (jog wheels) */
    @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    .jog-wheel {
        width: 150px; /* Tamanho ajustado para caber no layout */
        height: 150px;
        border-radius: 50%;
        background: conic-gradient(#1c1c1f, #333338, #1c1c1f, #333338);
        border: 6px solid #444449;
        margin: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: inset 0 0 15px rgba(0, 0, 0, 0.7);
        position: relative;
        animation: spin 8s linear infinite; /* Animação de rotação */
    }
    .jog-wheel::before {
        content: '';
        position: absolute;
        width: 30px;
        height: 30px;
        border-radius: 50%;
        background-color: #00aaff; /* Cor do LED central */
        box-shadow: 0 0 10px #00aaff;
    }
    
    /* Controles dentro do DJ table (botões, sliders) */
    .dj-controls-container {
        display: flex;
        gap: 20px; /* Espaçamento entre decks e mixer */
        width: 100%;
        height: 100%;
        align-items: center;
        justify-content: center;
    }
    .deck-section, .mixer-section {
        background-color: #1a1a1e; /* Fundo para os componentes individuais */
        border-radius: 8px;
        padding: 15px;
        border: 1px solid #2a2a2e;
        box-shadow: inset 0 0 8px rgba(0,0,0,0.4);
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 10px;
    }
    .deck-section {
        min-width: 250px;
    }
    .mixer-section {
        min-width: 150px;
    }

    /* LCD screens */
    .lcd-screen {
        background-color: #000;
        color: #00ff00; /* Verde néon */
        font-family: 'Digital-7', monospace; /* Fonte digital, se disponível */
        padding: 5px 10px;
        border: 1px solid #444;
        text-align: center;
        border-radius: 3px;
        margin-bottom: 10px;
        width: 90%;
        max-width: 200px;
        font-size: 0.8em;
    }

    /* Estilo dos sliders (personalizado para combinar com a estética) */
    .stSlider > div > div > div > div {
        background-color: #00aaff; /* Cor azul brilhante */
        height: 8px; /* Altura da barra do slider */
        border-radius: 4px;
    }
    .stSlider .st-emotion-cache-16j2u6n { /* Thumb do slider */
        background-color: #00aaff;
        border: 2px solid #fff;
        box-shadow: 0 0 5px rgba(0,0,0,0.5);
    }
    .stSlider label {
        color: #bbb; /* Cor das labels dos sliders */
        font-size: 0.8em;
    }

    /* Botões personalizados */
    .stButton > button {
        background-color: #333338;
        color: #e0e0e0;
        border: 1px solid #444449;
        border-radius: 5px;
        padding: 8px 12px;
        font-size: 0.9em;
        transition: all 0.2s ease-in-out;
        box-shadow: 0 2px 5px rgba(0,0,0,0.3);
    }
    .stButton > button:hover {
        background-color: #00aaff; /* Azul no hover */
        color: white;
        border-color: #00aaff;
        box-shadow: 0 0 10px rgba(0, 170, 255, 0.5);
        transform: translateY(-1px);
    }

    /* Coluna do navegador direito (SoundCloud Music Browser) */
    .right-browser-col {
        width: 300px; /* Largura fixa como na imagem */
        background-color: #2b2b30; /* Fundo igual ao da moldura */
        padding: 15px;
        border-left: 1px solid #3a3a3f;
        border-bottom-right-radius: 10px;
        overflow-y: auto; /* Rolagem para o conteúdo */
        flex-shrink: 0; /* Não encolher */
    }
    .right-browser-col h3 {
        color: #ffffff;
        margin-bottom: 15px;
        border-bottom: 1px solid #4a4a4f;
        padding-bottom: 10px;
    }
    .search-input-container {
        display: flex;
        gap: 5px;
        margin-bottom: 15px;
    }
    .stTextInput>div>div>input {
        background-color: #1a1a1e;
        color: #e0e0e0;
        border: 1px solid #3a3a3f;
        border-radius: 5px;
        padding: 8px 10px;
    }
    .stTextInput>div>div>input:focus {
        border-color: #00aaff;
        box-shadow: 0 0 0 2px rgba(0, 170, 255, 0.3);
    }
    .track-item {
        background-color: #1a1a1e;
        padding: 8px 10px;
        margin-bottom: 8px;
        border-radius: 5px;
        display: flex;
        align-items: center;
        gap: 10px;
        cursor: pointer;
        transition: background-color 0.2s ease;
    }
    .track-item:hover {
        background-color: #2b2b30;
    }
    .track-item .track-cover {
        width: 40px;
        height: 40px;
        border-radius: 3px;
        object-fit: cover;
    }
    .track-item .track-info strong {
        color: #ffffff;
        font-size: 0.9em;
    }
    .track-item .track-info small {
        color: #aaaaaa;
        font-size: 0.75em;
    }
</style>
""", unsafe_allow_html=True)

# --- Simulação de Ícones (em vez de carregar ficheiros) ---
# Em um ambiente real, você carregaria SVGs ou imagens.
# Aqui, usamos Unicode ou texto para representar.
def get_icon(name):
    icons = {
        "home": "🏠", "trending": "📈", "playlist": "🎵", "liked": "❤️",
        "station": "📻", "profile": "👤", "settings": "⚙️", "search": "🔍",
        "play": "▶️", "pause": "⏸️", "cue": "⏹️", "sync": "🔄", "loop": "🔁"
    }
    return icons.get(name, "")

# --- Conteúdo da Aplicação ---

# Simulação da moldura da janela da aplicação
st.markdown('<div class="app-frame">', unsafe_allow_html=True)

# Simulação da barra de título da janela
st.markdown("""
<div class="window-title-bar">
    <div class="traffic-lights">
        <div class="traffic-light red"></div>
        <div class="traffic-light yellow"></div>
        <div class="traffic-light green"></div>
    </div>
    <div class="app-name">SoundCloud - Gemini Digital DJ Deck</div>
    <span>SoundCloud</span>
</div>
""", unsafe_allow_html=True)

# Conteúdo principal com as 3 colunas
st.markdown('<div class="app-content">', unsafe_allow_html=True)

# --- COLUNA ESQUERDA: NAVEGADOR SOUNDCLOUD (simulado) ---
st.markdown('<div class="left-browser-col">', unsafe_allow_html=True)
st.markdown("<h3>SoundCloud</h3>", unsafe_allow_html=True)
st.markdown(f"""
    <div class="sidebar-item">{get_icon("home")} Testing Hive</div>
    <div class="sidebar-item">{get_icon("trending")} Trending Tracks</div>
    <div class="sidebar-item">{get_icon("playlist")} Playlists</div>
    <div class="sidebar-item">{get_icon("liked")} Liked Songs</div>
    <div class="sidebar-item">---</div>
    <div class="sidebar-item">{get_icon("station")} Station</div>
    <div class="sidebar-item">{get_icon("profile")} Profile</div>
    <div class="sidebar-item">{get_icon("settings")} Settings</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- COLUNA CENTRAL: MESA DE DJ ---
st.markdown('<div class="dj-deck-col">', unsafe_allow_html=True)
st.markdown("<h3>Gemini Digital DJ Deck</h3>", unsafe_allow_html=True)

# Barra de pesquisa acima da mesa de DJ (como na imagem)
st.text_input("🔍 Search tracks...", placeholder="Search for tracks or artists...", label_visibility="collapsed", key="top_search")

st.markdown('<div class="dj-table-placeholder">', unsafe_allow_html=True) # Retângulo preto grande

st.markdown('<div class="dj-controls-container">', unsafe_allow_html=True)

# DECK ESQUERDO (A)
st.markdown('<div class="deck-section">', unsafe_allow_html=True)
st.markdown('<div class="lcd-screen">TRACK A<br>--:-- / --:--</div>', unsafe_allow_html=True)
st.markdown('<div class="jog-wheel"></div>', unsafe_allow_html=True) # Disco de vinil animado
st.button(f"{get_icon('play')} Play", key="play_a", use_container_width=True)
st.button(f"{get_icon('cue')} Cue", key="cue_a", use_container_width=True)
st.slider("Volume A", 0.0, 1.0, 0.8, key="vol_a", format="%.2f")
st.slider("Pitch A", -0.10, 0.10, 0.0, key="pitch_a", format="%.2f")
st.markdown('</div>', unsafe_allow_html=True)

# MIXER CENTRAL
st.markdown('<div class="mixer-section">', unsafe_allow_html=True)
st.markdown("<h4>MIXER</h4>", unsafe_allow_html=True)
st.slider("Gain", 0, 100, 75, key="gain", label_visibility="collapsed")
st.markdown("---")
st.markdown("<h6>HI</h6>")
st.slider("High EQ", 0, 100, 50, key="hi_eq", label_visibility="collapsed")
st.markdown("<h6>MID</h6>")
st.slider("Mid EQ", 0, 100, 50, key="mid_eq", label_visibility="collapsed")
st.markdown("<h6>LOW</h6>")
st.slider("Low EQ", 0, 100, 50, key="low_eq", label_visibility="collapsed")
st.markdown("---")
st.markdown("<h6>CROSSFADER</h6>")
st.slider("Crossfader", -100, 100, 0, key="crossfader_val", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

# DECK DIREITO (B)
st.markdown('<div class="deck-section">', unsafe_allow_html=True)
st.markdown('<div class="lcd-screen">TRACK B<br>--:-- / --:--</div>', unsafe_allow_html=True)
st.markdown('<div class="jog-wheel"></div>', unsafe_allow_html=True) # Disco de vinil animado
st.button(f"{get_icon('play')} Play", key="play_b", use_container_width=True)
st.button(f"{get_icon('cue')} Cue", key="cue_b", use_container_width=True)
st.slider("Volume B", 0.0, 1.0, 0.8, key="vol_b", format="%.2f")
st.slider("Pitch B", -0.10, 0.10, 0.0, key="pitch_b", format="%.2f")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # Fecha dj-controls-container
st.markdown('</div>', unsafe_allow_html=True) # Fecha dj-table-placeholder
st.markdown('</div>', unsafe_allow_html=True) # Fecha dj-deck-col

# --- COLUNA DIREITA: SOUNDCLOUD MUSIC BROWSER (simulado) ---
st.markdown('<div class="right-browser-col">', unsafe_allow_html=True)
st.markdown("<h3>SoundCloud Music Browser</h3>", unsafe_allow_html=True)
search_soundcloud = st.text_input("Search SoundCloud...", placeholder="Search tracks, artists, genres...", key="soundcloud_search")

if search_soundcloud:
    st.markdown(f"**Results for '{search_soundcloud}':**")
    # Exemplo de resultados simulados
    st.markdown("""
        <div class="track-item">
            <img class="track-cover" src="https://via.placeholder.com/40" alt="Cover"/>
            <div class="track-info">
                <strong>Bohemian Rhapsody</strong><br>
                <small>Queen</small>
            </div>
        </div>
        <div class="track-item">
            <img class="track-cover" src="https://via.placeholder.com/40" alt="Cover"/>
            <div class="track-info">
                <strong>Stairway to Heaven</strong><br>
                <small>Led Zeppelin</small>
            </div>
        </div>
        <div class="track-item">
            <img class="track-cover" src="https://via.placeholder.com/40" alt="Cover"/>
            <div class="track-info">
                <strong>Shape of You</strong><br>
                <small>Ed Sheeran</small>
            </div>
            </div>
        <div class="track-item">
            <img class="track-cover" src="https://via.placeholder.com/40" alt="Cover"/>
            <div class="track-info">
                <strong>Blinding Lights</strong><br>
                <small>The Weeknd</small>
            </div>
        </div>
        <div class="track-item">
            <img class="track-cover" src="https://via.placeholder.com/40" alt="Cover"/>
            <div class="track-info">
                <strong>God's Plan</strong><br>
                <small>Drake</small>
            </div>
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <p style="color: #aaa; font-size: 0.9em;">Trending on SoundCloud:</p>
        <div class="track-item">
            <img class="track-cover" src="https://via.placeholder.com/40/00aaff/FFFFFF?text=T1" alt="Cover"/>
            <div class="track-info">
                <strong>Trending Track 1</strong><br>
                <small>Artist X</small>
            </div>
        </div>
        <div class="track-item">
            <img class="track-cover" src="https://via.placeholder.com/40/ff4b4b/FFFFFF?text=T2" alt="Cover"/>
            <div class="track-info">
                <strong>Hot Beat Tonight</strong><br>
                <small>Producer Y</small>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # Fecha right-browser-col

st.markdown('</div>', unsafe_allow_html=True) # Fecha app-content
st.markdown('</div>', unsafe_allow_html=True) # Fecha app-frame
