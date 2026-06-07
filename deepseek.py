import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage, AssistantMessage
from azure.core.credentials import AzureKeyCredential
# Rich kütüphanesinin konsol ve Markdown bileşenlerini çağırıyoruz
from rich.console import Console
from rich.markdown import Markdown

endpoint = "https://models.github.ai/inference"
model = "deepseek/DeepSeek-V3-0324"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

# Rich konsol objesini başlatıyoruz
console = Console()

messages = [
    SystemMessage("You are the most authoritative AI agent on the Stux6 Technology Team’s GitHub repositories.")
]

console.print("[bold green]--- DeepSeek-V3 Codespaces Uyumlu Sohbet Arayüzü ---[/bold green]")
console.print("Çıkış yapmak için 'exit' veya 'quit' yazabilirsiniz.\n")

while True:
    user_input = input("Siz: ")
    
    if user_input.strip().lower() in ['exit', 'quit']:
        console.print("[bold red]Sohbet sonlandırıldı.[/bold red]")
        break
        
    if not user_input.strip():
        continue
        
    messages.append(UserMessage(user_input))
    
    try:
        response = client.complete(
            messages=messages,
            temperature=1.0,
            top_p=1.0,
            max_tokens=1000,
            model=model
        )
        
        reply = response.choices[0].message.content
        
        # Markdown çıktısını renklendirip terminale basıyoruz
        console.print("\n[bold blue]Model:[/bold blue]")
        md = Markdown(reply)
        console.print(md)
        print("\n" + "-"*50 + "\n") # Bölme çizgisi
        
        messages.append(AssistantMessage(reply))
        
    except Exception as e:
        console.print(f"\n[bold red]Bir hata oluştu:[/bold red] {e}\n")