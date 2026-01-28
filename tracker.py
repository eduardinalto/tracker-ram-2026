import requests

def probar_busqueda_camuflada():
    print("🎭 Iniciando modo camuflaje total...")
    
    url = "https://api.mercadolibre.com/sites/MCO/search?q=ram+32gb+ddr4"
    
    # Esto hace que Mercado Libre crea que eres una persona real
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'application/json',
        'Accept-Language': 'es-CO,es;q=0.9',
    }
    
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        resultados = data.get('results', [])
        
        print(f"📦 ¡Detección final!: {len(resultados)} productos encontrados.")

        if len(resultados) > 0:
            print("-" * 40)
            for item in resultados[:3]:
                print(f"📍 {item.get('title')[:35]}...")
                print(f"💰 Precio: ${item.get('price'):,.0f}")
                print("-" * 40)
        else:
            print("❗ Sigue en 0. Mercado Libre está bloqueando tu IP local para procesos automáticos.")
            
    except Exception as e:
        print(f"💥 Error: {e}")

if __name__ == "__main__":
    probar_busqueda_camuflada()