import re
import sys

import requests
from bs4 import BeautifulSoup, FeatureNotFound

RSS_URL = "https://www.yna.co.kr/rss/news.xml"
LIMIT = 10


def parse_rss(xml_text: str) -> BeautifulSoup:
    try:
        return BeautifulSoup(xml_text, "xml")
    except FeatureNotFound:
        return BeautifulSoup(xml_text, "html.parser")


def clean_summary(raw_html: str) -> str:
    if not raw_html:
        return "(요약 없음)"
    text = BeautifulSoup(raw_html, "html.parser").get_text(" ", strip=True)
    return text or "(요약 없음)"


def fetch_news(url: str, limit: int = 10):
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = parse_rss(response.text)
    items = soup.find_all("item")[:limit]

    news_list = []
    for item in items:
        title = item.title.get_text(strip=True) if item.title else "(제목 없음)"
        link = item.link.get_text(strip=True) if item.link else "(링크 없음)"
        pub_date = item.pubDate.get_text(strip=True) if item.pubDate else "(발행시간 없음)"
        summary = clean_summary(item.description.get_text() if item.description else "")

        news_list.append(
            {
                "title": title,
                "summary": summary,
                "link": link,
                "pub_date": pub_date,
            }
        )

    return news_list


def print_news(news_list):
    print(f"총 {len(news_list)}건\n")
    for idx, news in enumerate(news_list, 1):
        print(f"[{idx}] {news['title']}")
        print(f"  - 요약: {news['summary']}")
        print(f"  - 링크: {news['link']}")
        print(f"  - 발행: {news['pub_date']}")
        print("-" * 80)


def extract_article_text(url: str, max_chars: int = 1200) -> str:
    response = requests.get(
        url,
        timeout=10,
        headers={"User-Agent": "Mozilla/5.0"},
        allow_redirects=True,
    )
    response.raise_for_status()

    final_url = response.url
    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    candidates = soup.select("article p, #articleBody p, .article p, .story p, p")
    paragraphs = []
    for p in candidates:
        text = re.sub(r"\s+", " ", p.get_text(" ", strip=True))
        if len(text) >= 40:
            paragraphs.append(text)

    if not paragraphs:
        body_text = re.sub(r"\s+", " ", soup.get_text(" ", strip=True))
        preview = body_text[:max_chars] + ("..." if len(body_text) > max_chars else "")
        return f"[원문 URL] {final_url}\n\n{preview}"

    joined = "\n".join(paragraphs[:8])
    preview = joined[:max_chars] + ("..." if len(joined) > max_chars else "")
    return f"[원문 URL] {final_url}\n\n{preview}"


def show_selected_article_content(news_list):
    if not news_list:
        print("기사 목록이 없습니다.")
        return

    while True:
        selected = input(f"\n본문으로 볼 기사 번호를 입력하세요 (1-{len(news_list)}, 종료=q): ").strip()

        if selected.lower() == "q":
            print("종료합니다.")
            return

        if not selected.isdigit():
            print("숫자 또는 q를 입력해 주세요.")
            continue

        idx = int(selected)
        if not (1 <= idx <= len(news_list)):
            print(f"1부터 {len(news_list)} 사이 번호를 입력해 주세요.")
            continue

        article = news_list[idx - 1]
        print("\n" + "=" * 80)
        print(f"[본문 미리보기] {article['title']}")
        print(f"원문 링크: {article['link']}")
        print("-" * 80)

        try:
            content = extract_article_text(article["link"])
            print(content if content else "본문을 추출하지 못했습니다.")
        except requests.RequestException as e:
            print(f"기사 본문 요청 중 오류가 발생했습니다: {e}")

        print("=" * 80)
        return


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    try:
        news = fetch_news(RSS_URL, LIMIT)
        print_news(news)
        show_selected_article_content(news)
    except requests.RequestException as e:
        print(f"RSS 요청 중 오류가 발생했습니다: {e}")


if __name__ == "__main__":
    main()
