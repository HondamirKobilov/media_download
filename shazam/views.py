import httpx
from django.http import JsonResponse
from django.shortcuts import render

def index(request):
    return render(request, 'shazam/index.html')

async def fetch_instagram_media(request):
    url = request.GET.get("url")
    if not url:
        return JsonResponse({"error": True, "message": "URL kiritilmagan."}, status=400)
    try:
        api_url = f"https://fast.videoyukla.uz/instagram/media?in_url={url}"
        async with httpx.AsyncClient() as client:
            response = await client.get(api_url)
        return JsonResponse(response.json())
    except Exception as e:
        return JsonResponse({"error": True, "message": str(e)}, status=500)