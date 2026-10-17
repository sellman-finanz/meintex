#!/usr/bin/env python3
"""Erzeugt en.html und tr.html aus der deutschen index.html.

Nach jeder Änderung an index.html neu ausführen:
    python3 build-lang.py

Jede Zeile in T ist (Deutsch, Englisch, Türkisch). Wird ein deutscher Text
in index.html nicht mehr gefunden, meldet das Skript ihn, damit die
Übersetzung angepasst werden kann.
"""
from pathlib import Path

HERE = Path(__file__).parent

T = [
    # Kopf
    ('<html lang="de">', '<html lang="en">', '<html lang="tr">'),
    ('<title>MEINTEX – B2B Textilproduktion & Sourcing für Marken und Unternehmen</title>',
     '<title>MEINTEX – B2B Textile Production & Sourcing for Brands and Businesses</title>',
     '<title>MEINTEX – Markalar ve Firmalar için B2B Tekstil Üretimi & Tedarik</title>'),
    ('content="MEINTEX ist Ihr B2B-Partner für Textilproduktion in Serie: Sampling, Bulk Production und Repeat Orders ab 500 Stück. Produktionsschwerpunkt Türkei, Projektsteuerung für Deutschland und die EU."',
     'content="MEINTEX is your B2B partner for textile series production: sampling, bulk production and repeat orders from 500 pieces. Production focus in Turkey, project management for Germany and the EU."',
     'content="MEINTEX, seri tekstil üretiminde B2B ortağınızdır: 500 adetten itibaren numune, toplu üretim ve tekrar siparişler. Üretim Türkiye\'de, proje yönetimi Almanya ve AB için."'),

    # Navigation
    ('<a href="#zielgruppen">Für wen</a>', '<a href="#zielgruppen">Who we serve</a>', '<a href="#zielgruppen">Kimler için</a>'),
    ('<a href="#leistungen">Leistungen</a>', '<a href="#leistungen">Services</a>', '<a href="#leistungen">Hizmetler</a>'),
    ('<a href="#prozess">Prozess</a>', '<a href="#prozess">Process</a>', '<a href="#prozess">Süreç</a>'),
    ('<a href="#mengen">Mengen</a>', '<a href="#mengen">Quantities</a>', '<a href="#mengen">Adetler</a>'),
    ('<a href="#faq">FAQ</a>', '<a href="#faq">FAQ</a>', '<a href="#faq">SSS</a>'),
    ('aria-label="Menü"', 'aria-label="Menu"', 'aria-label="Menü"'),

    # Hero
    ('<h1>Textilproduktion in Serie für Marken &amp; Unternehmen.</h1>',
     '<h1>Textile series production for brands &amp; businesses.</h1>',
     '<h1>Markalar ve firmalar için seri tekstil üretimi.</h1>'),
    ('<p>Von der ersten Idee über das Muster bis zur Großserie: Wir steuern Ihre Produktion in der Türkei und liefern nach Deutschland und in die EU.</p>',
     '<p>From the first idea to the sample to large-scale production: we manage your production in Turkey and deliver to Germany and the EU.</p>',
     '<p>İlk fikirden numuneye, numuneden büyük seri üretime: Üretiminizi Türkiye\'de yönetiyor, Almanya ve AB\'ye teslim ediyoruz.</p>'),
    ('Projekt anfragen →', 'Request a project →', 'Proje talebi →'),
    ('>So arbeiten wir<', '>How we work<', '>Nasıl çalışıyoruz<'),
    ('Sampling <span class="arrow">→</span> Serienproduktion <span class="arrow">→</span>',
     'Sampling <span class="arrow">→</span> Series production <span class="arrow">→</span>',
     'Numune <span class="arrow">→</span> Seri üretim <span class="arrow">→</span>'),

    # Kennzahlen
    ('<b>ab 500</b><span>Stück pro Projekt</span>', '<b>from 500</b><span>pieces per project</span>', '<b>500\'den</b><span>itibaren adet / proje</span>'),
    ('<span>von Design bis Lieferung</span>', '<span>from design to delivery</span>', '<span>tasarımdan teslimata</span>'),
    ('<span>Produktion &amp; Projektsteuerung</span>', '<span>production &amp; project management</span>', '<span>üretim &amp; proje yönetimi</span>'),
    ('<span>skalierbare Nachbestellungen</span>', '<span>scalable reorders</span>', '<span>ölçeklenebilir tekrar siparişler</span>'),

    # Zielgruppen
    ('>Für wen wir produzieren<', '>Who we produce for<', '>Kimler için üretiyoruz<'),
    ('>Ein Production House für Brands &amp; Businesses.<', '>A production house for brands &amp; businesses.<', '>Markalar ve firmalar için bir üretim evi.<'),
    ('>Wir arbeiten mit Unternehmen, die Textilien in Serie brauchen, oft mit wiederkehrendem Jahresbedarf.<',
     '>We work with companies that need textiles in series, often with recurring annual demand.<',
     '>Seri halinde tekstile ihtiyaç duyan, çoğu zaman yıllık düzenli talebi olan firmalarla çalışıyoruz.<'),
    ('<p>Für Großhändler, Distributoren und Handelsunternehmen mit regelmäßigem Textileinkauf.</p>',
     '<p>For wholesalers, distributors and retailers with regular textile purchasing.</p>',
     '<p>Düzenli tekstil alımı yapan toptancılar, distribütörler ve ticaret firmaları için.</p>'),
    ('<p>Mitarbeiterbekleidung für Industrie, Logistik, Facility, Hotellerie, Gastronomie und Filialisten.</p>',
     '<p>Staff clothing for industry, logistics, facility management, hotels, restaurants and retail chains.</p>',
     '<p>Sanayi, lojistik, tesis yönetimi, otelcilik, gastronomi ve zincir mağazalar için personel kıyafetleri.</p>'),
    ('<p>Für Fashion-Brands, Designer und Onlinehändler: Entwicklung, Sampling und Kollektion.</p>',
     '<p>For fashion brands, designers and online retailers: development, sampling and collections.</p>',
     '<p>Moda markaları, tasarımcılar ve online satıcılar için: geliştirme, numune ve koleksiyon.</p>'),
    ('<p>Für Vereine, Sportorganisationen und Teamwear-Händler, individualisiert und nachbestellbar.</p>',
     '<p>For clubs, sports organisations and teamwear retailers, customised and reorderable.</p>',
     '<p>Kulüpler, spor organizasyonları ve takım giyim satıcıları için; kişiselleştirilmiş ve tekrar sipariş edilebilir.</p>'),
    ('<p>Für Merch-Händler, Agenturen und Unternehmen: Kampagnenmengen mit Ihrem Branding.</p>',
     '<p>For merch retailers, agencies and companies: campaign quantities with your branding.</p>',
     '<p>Merch satıcıları, ajanslar ve firmalar için: markanızla kampanya adetleri.</p>'),
    ('<h3>Rahmenverträge</h3>', '<h3>Framework contracts</h3>', '<h3>Çerçeve sözleşmeler</h3>'),
    ('<p>Für Ausschreibungen, Rahmenbedarfe und wiederkehrende Abrufbestellungen.</p>',
     '<p>For tenders, framework requirements and recurring call-off orders.</p>',
     '<p>İhaleler, çerçeve ihtiyaçlar ve düzenli çağrı siparişleri için.</p>'),
    ('1.000 bis 500.000+ Stück', '1,000 to 500,000+ pieces', '1.000 – 500.000+ adet'),
    ('500 bis 100.000+ Stück', '500 to 100,000+ pieces', '500 – 100.000+ adet'),
    ('500 bis 50.000+ Stück', '500 to 50,000+ pieces', '500 – 50.000+ adet'),
    ('1.000 bis 100.000+ Stück', '1,000 to 100,000+ pieces', '1.000 – 100.000+ adet'),
    ('>nach individueller Prüfung<', '>after individual review<', '>bireysel değerlendirme sonrası<'),

    # Split
    ('alt="Stickmaschine bestickt einen Hoodie"', 'alt="Embroidery machine stitching a hoodie"', 'alt="Nakış makinesi bir sweatshirt işliyor"'),
    ('>Produktion Türkei · Steuerung Deutschland<', '>Production Turkey · Management Germany<', '>Üretim Türkiye · Yönetim Almanya<'),
    ('<h2>Kurze Wege zur Produktion. Ein Ansprechpartner hier.</h2>',
     '<h2>Short routes to production. One contact person here.</h2>',
     '<h2>Üretime kısa yol. Burada tek bir muhatap.</h2>'),
    ('>Unsere Produktion läuft mit ausgewählten Partnerbetrieben in der Türkei. MEINTEX koordiniert das Projekt von Deutschland aus, persönlich und in Ihrer Sprache.<',
     '>We produce with selected partner factories in Turkey. MEINTEX coordinates your project from Germany, personally and in your language.<',
     '>Üretimimiz Türkiye\'deki seçkin partner atölyelerle yapılır. MEINTEX projenizi Almanya\'dan, birebir ve sizin dilinizde koordine eder.<'),
    ('<li>Projektklärung, Spezifikation und Tech-Pack-Abstimmung</li>', '<li>Project briefing, specification and tech pack alignment</li>', '<li>Proje netleştirme, spesifikasyon ve tech pack uyumu</li>'),
    ('<li>Muster vor der Serienfreigabe</li>', '<li>Samples before series approval</li>', '<li>Seri onayından önce numune</li>'),
    ('<li>Produktionsbegleitung und Qualitätskontrolle vor Ort</li>', '<li>On-site production supervision and quality control</li>', '<li>Yerinde üretim takibi ve kalite kontrol</li>'),
    ('<li>Verpackung, Versand und Logistik nach Deutschland/EU</li>', '<li>Packaging, shipping and logistics to Germany/EU</li>', '<li>Almanya/AB\'ye paketleme, sevkiyat ve lojistik</li>'),

    # Hinter den Kulissen
    ('>Hinter den Kulissen<', '>Behind the scenes<', '>Perde arkası<'),
    ('>Handwerk, Maschinen und Kontrolle. Stück für Stück.<', '>Craft, machines and control. Piece by piece.<', '>Zanaat, makine ve kontrol. Parça parça.<'),
    ('>Nähen, Sticken, Drucken, Prüfen und Verpacken: In unseren Partnerbetrieben entsteht jedes Teil nach Ihrer Spezifikation. Wir begleiten die Produktion und kontrollieren die Qualität, bevor Ihre Ware auf den Weg geht.<',
     '>Sewing, embroidery, printing, inspection and packing: in our partner factories every piece is made to your specification. We supervise production and check quality before your goods are shipped.<',
     '>Dikiş, nakış, baskı, kontrol ve paketleme: Partner atölyelerimizde her parça sizin spesifikasyonunuza göre üretilir. Üretimi takip eder, ürünleriniz yola çıkmadan önce kaliteyi kontrol ederiz.<'),
    ('<b>Nähen</b><span>Serienfertigung</span>', '<b>Sewing</b><span>series production</span>', '<b>Dikiş</b><span>seri üretim</span>'),
    ('<b>Veredelung</b><span>Stick, Siebdruck, DTF, DTG</span>', '<b>Finishing</b><span>embroidery, screen print, DTF, DTG</span>', '<b>Baskı & nakış</b><span>nakış, serigrafi, DTF, DTG</span>'),
    ('<span>Prüfung vor Versand</span>', '<span>inspection before shipping</span>', '<span>sevkiyat öncesi kontrol</span>'),
    ('<b>Verpackung</b><span>Private Label &amp; Logistik</span>', '<b>Packaging</b><span>private label &amp; logistics</span>', '<b>Paketleme</b><span>private label &amp; lojistik</span>'),

    # Leistungen
    ('<span class="eyebrow reveal">Leistungen</span>', '<span class="eyebrow reveal">Services</span>', '<span class="eyebrow reveal">Hizmetler</span>'),
    ('>Alles aus einer Hand.<', '>Everything from one source.<', '>Her şey tek elden.<'),
    ('>Fashion, Menswear, Womenswear, Kidswear, Sportswear, Workwear, Corporate Wear und Merchandise.<',
     '>Fashion, menswear, womenswear, kidswear, sportswear, workwear, corporate wear and merchandise.<',
     '>Moda, erkek, kadın ve çocuk giyim, spor giyim, iş kıyafetleri, kurumsal giyim ve promosyon ürünleri.<'),
    ('<h3>Beratung</h3><p>Vom Bedarf bis zur Produktionsfreigabe: Wir klären Produkt, Menge, Material und Timing.</p>',
     '<h3>Consulting</h3><p>From requirement to production approval: we clarify product, quantity, material and timing.</p>',
     '<h3>Danışmanlık</h3><p>İhtiyaçtan üretim onayına: Ürün, adet, malzeme ve zamanlamayı birlikte netleştiriyoruz.</p>'),
    ('<h3>Design &amp; Entwicklung</h3><p>Grafik- und Modedesign, Produktentwicklung, Tech Packs und Spezifikationen.</p>',
     '<h3>Design &amp; development</h3><p>Graphic and fashion design, product development, tech packs and specifications.</p>',
     '<h3>Tasarım &amp; geliştirme</h3><p>Grafik ve moda tasarımı, ürün geliştirme, tech pack ve spesifikasyonlar.</p>'),
    ('<h3>Sampling</h3><p>Musterentwicklung vor der Serie, damit Passform, Stoff und Farbe stimmen.</p>',
     '<h3>Sampling</h3><p>Sample development before series production, so fit, fabric and colour are right.</p>',
     '<h3>Numune</h3><p>Kalıp, kumaş ve renk doğru olsun diye seri öncesi numune geliştirme.</p>'),
    ('<h3>Serienproduktion</h3><p>Skalierbare Produktion vom Serienauftrag bis zum Großprojekt.</p>',
     '<h3>Series production</h3><p>Scalable production from series orders to large projects.</p>',
     '<h3>Seri üretim</h3><p>Seri siparişten büyük projeye kadar ölçeklenebilir üretim.</p>'),
    ('<h3>Veredelung</h3><p>Stick, Siebdruck, DTF und DTG, je nach Produkt und Projekt.</p>',
     '<h3>Finishing</h3><p>Embroidery, screen printing, DTF and DTG, depending on product and project.</p>',
     '<h3>Baskı &amp; nakış</h3><p>Ürüne ve projeye göre nakış, serigrafi, DTF ve DTG.</p>'),
    ('<h3>Private Label</h3><p>Markenetiketten, Hangtags, individuelle Verpackung und Branding.</p>',
     '<h3>Private label</h3><p>Brand labels, hangtags, custom packaging and branding.</p>',
     '<h3>Private label</h3><p>Marka etiketleri, askı etiketleri, özel ambalaj ve markalama.</p>'),
    ('<h3>Qualitätskontrolle</h3><p>Laufende Produktionsbegleitung und Prüfung vor dem Versand.</p>',
     '<h3>Quality control</h3><p>Ongoing production supervision and inspection before shipping.</p>',
     '<h3>Kalite kontrol</h3><p>Sürekli üretim takibi ve sevkiyat öncesi kontrol.</p>'),
    ('<h3>Logistik &amp; Repeat</h3><p>Versand nach Deutschland/EU und unkomplizierte Nachbestellungen.</p>',
     '<h3>Logistics &amp; repeat</h3><p>Shipping to Germany/EU and easy reorders.</p>',
     '<h3>Lojistik &amp; tekrar</h3><p>Almanya/AB\'ye sevkiyat ve kolay tekrar siparişler.</p>'),

    # Prozess
    ('<span class="eyebrow reveal">Prozess</span>', '<span class="eyebrow reveal">Process</span>', '<span class="eyebrow reveal">Süreç</span>'),
    ('>Von der Anfrage bis zur Lieferung.<', '>From enquiry to delivery.<', '>Talepten teslimata.<'),
    ('<h3>Anfrage</h3><p>Sie schildern Produkt, Menge und Termin.</p>', '<h3>Enquiry</h3><p>You describe product, quantity and deadline.</p>', '<h3>Talep</h3><p>Ürünü, adedi ve tarihi bize iletirsiniz.</p>'),
    ('<h3>Qualifizierung</h3><p>Wir prüfen Machbarkeit und melden uns persönlich.</p>', '<h3>Qualification</h3><p>We check feasibility and get back to you personally.</p>', '<h3>Değerlendirme</h3><p>Uygulanabilirliği kontrol eder, size bizzat döneriz.</p>'),
    ('<h3>Spezifikation</h3><p>Material, Größen, Branding, Tech Pack.</p>', '<h3>Specification</h3><p>Material, sizes, branding, tech pack.</p>', '<h3>Spesifikasyon</h3><p>Malzeme, bedenler, markalama, tech pack.</p>'),
    ('<h3>Sampling</h3><p>Muster zur Abnahme vor der Serie.</p>', '<h3>Sampling</h3><p>Samples for approval before the series.</p>', '<h3>Numune</h3><p>Seri öncesi onay için numune.</p>'),
    ('<h3>Freigabe</h3><p>Angebot, Lieferfenster und Produktionsplan.</p>', '<h3>Approval</h3><p>Quote, delivery window and production plan.</p>', '<h3>Onay</h3><p>Teklif, teslim aralığı ve üretim planı.</p>'),
    ('<h3>Produktion &amp; QC</h3><p>Serienfertigung mit Qualitätskontrolle.</p>', '<h3>Production &amp; QC</h3><p>Series production with quality control.</p>', '<h3>Üretim &amp; KK</h3><p>Kalite kontrollü seri üretim.</p>'),
    ('<h3>Versand</h3><p>Verpackt und geliefert nach DE/EU.</p>', '<h3>Shipping</h3><p>Packed and delivered to DE/EU.</p>', '<h3>Sevkiyat</h3><p>Paketlenip DE/AB\'ye teslim.</p>'),

    # Mengen
    ('<span class="eyebrow reveal">Mengen</span>', '<span class="eyebrow reveal">Quantities</span>', '<span class="eyebrow reveal">Adetler</span>'),
    ('>Vom Serienauftrag bis zum Rahmenprojekt.<', '>From series orders to framework projects.<', '>Seri siparişten çerçeve projeye.<'),
    ('>Je größer die Serie, desto wichtiger die Planung. Großprojekte prüfen wir individuell auf Kapazität, Material und Lieferfenster.<',
     '>The bigger the series, the more planning matters. We review large projects individually for capacity, material and delivery window.<',
     '>Seri büyüdükçe planlama daha da önemli hale gelir. Büyük projeleri kapasite, malzeme ve teslim aralığı açısından ayrı ayrı değerlendiririz.<'),
    ('<b>1.000 – 9.999</b>', '<b>1,000 – 9,999</b>', '<b>1.000 – 9.999</b>'),
    ('<b>10.000 – 99.999</b>', '<b>10,000 – 99,999</b>', '<b>10.000 – 99.999</b>'),
    ('<b>100.000 – 499.999</b>', '<b>100,000 – 499,999</b>', '<b>100.000 – 499.999</b>'),
    ('<b>500.000+</b>', '<b>500,000+</b>', '<b>500.000+</b>'),
    ('<span>Einstieg für B2B-Projekte mit klarer Spezifikation</span>', '<span>Entry level for B2B projects with a clear specification</span>', '<span>Net spesifikasyonlu B2B projeler için başlangıç</span>'),
    ('<span>Serienaufträge, ideal mit wiederkehrendem Bedarf</span>', '<span>Series orders, ideally with recurring demand</span>', '<span>Seri siparişler, ideal olarak düzenli talep ile</span>'),
    ('<span>Großaufträge mit persönlicher Projektbetreuung</span>', '<span>Large orders with personal project support</span>', '<span>Kişisel proje desteğiyle büyük siparişler</span>'),
    ('<span>Strategische Großprojekte mit individueller Kapazitätsplanung</span>', '<span>Strategic large projects with individual capacity planning</span>', '<span>Bireysel kapasite planlamalı stratejik büyük projeler</span>'),
    ('<span>Großserien und Rahmenprojekte nach individueller Kapazitätsprüfung</span>', '<span>Large series and framework projects after individual capacity review</span>', '<span>Bireysel kapasite kontrolü sonrası büyük seriler ve çerçeve projeler</span>'),
    ('>Preise, Kapazitäten und Lieferzeiten nennen wir nach Prüfung Ihres konkreten Projekts.<',
     '>We quote prices, capacities and lead times after reviewing your specific project.<',
     '>Fiyat, kapasite ve teslim sürelerini somut projenizi inceledikten sonra bildiririz.<'),

    # Referenzen
    ('>Referenzen<', '>References<', '>Referanslar<'),
    ('>Marken, die mit uns produzieren.<', '>Brands that produce with us.<', '>Bizimle üretim yapan markalar.<'),

    # FAQ
    ('>Häufige Fragen.<', '>Frequently asked questions.<', '>Sık sorulan sorular.<'),
    ('<summary>Was ist die Mindestbestellmenge (MOQ)?</summary><p>Wir starten ab 500 Stück pro Projekt. Die genaue MOQ hängt von Produkt, Material und Veredelung ab.</p>',
     '<summary>What is the minimum order quantity (MOQ)?</summary><p>We start from 500 pieces per project. The exact MOQ depends on product, material and finishing.</p>',
     '<summary>Minimum sipariş adedi (MOQ) nedir?</summary><p>Proje başına 500 adetten başlıyoruz. Kesin MOQ ürüne, malzemeye ve baskı/nakışa göre değişir.</p>'),
    ('<summary>Bekomme ich vor der Serie ein Muster?</summary><p>Ja. Vor jeder Serienproduktion entwickeln wir ein Muster, das Sie prüfen und freigeben. Kosten und Dauer des Samplings nennen wir projektbezogen.</p>',
     '<summary>Do I get a sample before the series?</summary><p>Yes. Before every series production we develop a sample for you to review and approve. Sampling costs and duration depend on the project.</p>',
     '<summary>Seri öncesi numune alabilir miyim?</summary><p>Evet. Her seri üretimden önce inceleyip onaylamanız için bir numune hazırlarız. Numune maliyeti ve süresi projeye göre belirlenir.</p>'),
    ('<summary>Wie lange dauert die Produktion?</summary><p>Das hängt von Menge, Produkt und Material ab. Nach der Projektprüfung erhalten Sie ein konkretes Lieferfenster.</p>',
     '<summary>How long does production take?</summary><p>That depends on quantity, product and material. After reviewing your project you receive a concrete delivery window.</p>',
     '<summary>Üretim ne kadar sürer?</summary><p>Adet, ürün ve malzemeye bağlıdır. Proje değerlendirmesinden sonra size somut bir teslim aralığı bildiririz.</p>'),
    ('<summary>Welche Veredelungen bieten Sie an?</summary><p>Unter anderem Stick, Siebdruck, DTF und DTG. Dazu Private-Label-Elemente wie Etiketten, Hangtags und Verpackung.</p>',
     '<summary>Which finishing options do you offer?</summary><p>Among others embroidery, screen printing, DTF and DTG, plus private label elements such as labels, hangtags and packaging.</p>',
     '<summary>Hangi baskı ve nakış seçeneklerini sunuyorsunuz?</summary><p>Nakış, serigrafi, DTF ve DTG gibi seçeneklerin yanı sıra etiket, askı etiketi ve ambalaj gibi private label öğeleri.</p>'),
    ('<summary>Wo wird produziert?</summary><p>Der Produktionsschwerpunkt liegt in der Türkei bei ausgewählten Partnerbetrieben. MEINTEX übernimmt Projektsteuerung, Qualitätskontrolle und Logistik nach Deutschland und in die EU.</p>',
     '<summary>Where is production based?</summary><p>Production is focused in Turkey with selected partner factories. MEINTEX handles project management, quality control and logistics to Germany and the EU.</p>',
     '<summary>Üretim nerede yapılıyor?</summary><p>Üretim ağırlıklı olarak Türkiye\'de seçkin partner atölyelerde yapılır. MEINTEX proje yönetimini, kalite kontrolü ve Almanya ile AB\'ye lojistiği üstlenir.</p>'),
    ('<summary>Sind auch sehr große Mengen möglich?</summary><p>Ja, wir nehmen Anfragen bis 500.000+ Stück entgegen. Großserien und Rahmenprojekte planen wir nach individueller Kapazitätsprüfung.</p>',
     '<summary>Are very large quantities possible?</summary><p>Yes, we accept enquiries up to 500,000+ pieces. We plan large series and framework projects after an individual capacity review.</p>',
     '<summary>Çok büyük adetler de mümkün mü?</summary><p>Evet, 500.000+ adede kadar talepleri kabul ediyoruz. Büyük seri ve çerçeve projeleri bireysel kapasite kontrolünden sonra planlıyoruz.</p>'),

    # Anfrage
    ('<span class="eyebrow">Projekt anfragen</span>', '<span class="eyebrow">Request a project</span>', '<span class="eyebrow">Proje talebi</span>'),
    ('>Erzählen Sie uns von Ihrem Projekt.<', '>Tell us about your project.<', '>Bize projenizden bahsedin.<'),
    ('>Je genauer Ihre Angaben, desto schneller können wir Ihnen ein belastbares Angebot machen. Wir melden uns persönlich.<',
     '>The more detail you give, the faster we can send you a reliable quote. We will get back to you personally.<',
     '>Bilgileriniz ne kadar ayrıntılı olursa size o kadar hızlı ve sağlam bir teklif sunabiliriz. Size bizzat dönüş yapacağız.<'),
    ('WhatsApp schreiben', 'Message on WhatsApp', 'WhatsApp\'tan yazın'),
    ('<label>Firma *</label>', '<label>Company *</label>', '<label>Firma *</label>'),
    ('<label>Ansprechpartner *</label>', '<label>Contact person *</label>', '<label>Yetkili kişi *</label>'),
    ('<label>Ihre Rolle</label>', '<label>Your role</label>', '<label>Göreviniz</label>'),
    ('<option>Einkauf</option><option>Geschäftsführung</option><option>Marke / Brand</option><option>Agentur</option><option>Sonstiges</option>',
     '<option>Purchasing</option><option>Management</option><option>Brand</option><option>Agency</option><option>Other</option>',
     '<option>Satın alma</option><option>Yönetim</option><option>Marka</option><option>Ajans</option><option>Diğer</option>'),
    ('<label>Geschäftliche E-Mail *</label>', '<label>Business email *</label>', '<label>Kurumsal e-posta *</label>'),
    ('<label>Telefon</label>', '<label>Phone</label>', '<label>Telefon</label>'),
    ('<label>Produktart *</label>', '<label>Product type *</label>', '<label>Ürün türü *</label>'),
    ('placeholder="z. B. T-Shirts, Hoodies, Poloshirts"', 'placeholder="e.g. T-shirts, hoodies, polo shirts"', 'placeholder="ör. tişört, sweatshirt, polo yaka"'),
    ('<label>Geplante Erstbestellung *</label>', '<label>Planned first order *</label>', '<label>Planlanan ilk sipariş *</label>'),
    ('<option value="">Bitte wählen</option>', '<option value="">Please select</option>', '<option value="">Lütfen seçin</option>'),
    ('<label>Bestellart</label>', '<label>Order type</label>', '<label>Sipariş türü</label>'),
    ('<option>Einmalige Bestellung</option><option>Wiederkehrender Bedarf</option><option>Rahmenvertrag / Abruf</option>',
     '<option>One-off order</option><option>Recurring demand</option><option>Framework contract / call-off</option>',
     '<option>Tek seferlik sipariş</option><option>Düzenli ihtiyaç</option><option>Çerçeve sözleşme / çağrı</option>'),
    ('<label>Geschätzter Jahresbedarf</label>', '<label>Estimated annual demand</label>', '<label>Tahmini yıllık ihtiyaç</label>'),
    ('placeholder="Stück pro Jahr"', 'placeholder="pieces per year"', 'placeholder="yıllık adet"'),
    ('placeholder="Druck, Stick, Private Label …"', 'placeholder="print, embroidery, private label …"', 'placeholder="baskı, nakış, private label …"'),
    ('<label>Tech Pack / Muster vorhanden?</label>', '<label>Tech pack / sample available?</label>', '<label>Tech pack / numune var mı?</label>'),
    ('<option>Nein</option><option>Ja, Tech Pack</option><option>Ja, Muster / Referenzprodukt</option>',
     '<option>No</option><option>Yes, tech pack</option><option>Yes, sample / reference product</option>',
     '<option>Hayır</option><option>Evet, tech pack</option><option>Evet, numune / referans ürün</option>'),
    ('<label>Wunschtermin</label>', '<label>Preferred date</label>', '<label>İstenen tarih</label>'),
    ('<label>Lieferland</label><input name="Lieferland" value="Deutschland">', '<label>Delivery country</label><input name="Lieferland" value="Germany">', '<label>Teslimat ülkesi</label><input name="Lieferland" value="Almanya">'),
    ('<label>Projektbeschreibung</label>', '<label>Project description</label>', '<label>Proje açıklaması</label>'),
    ('placeholder="Material, Grammatur, Farben, Größen, besondere Anforderungen …"', 'placeholder="material, fabric weight, colours, sizes, special requirements …"', 'placeholder="malzeme, gramaj, renkler, bedenler, özel istekler …"'),
    ('Logo, Tech Pack oder Referenzbilder schicken Sie uns gern direkt an <a href="mailto:info@meintex.de">info@meintex.de</a> oder per WhatsApp.',
     'Feel free to send your logo, tech pack or reference images directly to <a href="mailto:info@meintex.de">info@meintex.de</a> or via WhatsApp.',
     'Logo, tech pack veya referans görsellerinizi doğrudan <a href="mailto:info@meintex.de">info@meintex.de</a> adresine ya da WhatsApp\'tan gönderebilirsiniz.'),
    ('value="Neue Projektanfrage über meintex.de"', 'value="New project enquiry via meintex.de (EN)"', 'value="meintex.de üzerinden yeni proje talebi (TR)"'),
    ('Ich stimme zu, dass meine Angaben zur Bearbeitung der Anfrage gespeichert werden. Details in der <a href="#">Datenschutzerklärung</a>.',
     'I agree that my details will be stored to process this enquiry. Details in the <a href="#">privacy policy</a>.',
     'Bilgilerimin talebin işlenmesi için saklanmasını kabul ediyorum. Ayrıntılar <a href="#">gizlilik politikasında</a>.'),
    ('Anfrage senden →', 'Send enquiry →', 'Talebi gönder →'),

    # Footer
    ('<h4>Kontakt</h4>', '<h4>Contact</h4>', '<h4>İletişim</h4>'),
    ('<h4>Unternehmen</h4>', '<h4>Company</h4>', '<h4>Şirket</h4>'),
    ('<a href="impressum.html">Impressum</a> · <a href="#">Datenschutz</a>', '<a href="impressum.html">Legal notice</a> · <a href="#">Privacy</a>', '<a href="impressum.html">Künye</a> · <a href="#">Gizlilik</a>'),

    # Skript-Texte und Formular-Technik
    ('<input type="hidden" name="Sprache" value="DE">', '<input type="hidden" name="Sprache" value="EN">', '<input type="hidden" name="Sprache" value="TR">'),
    ('<label>Nicht ausfüllen: ', '<label>Do not fill in: ', '<label>Doldurmayın: '),
    ("'Vielen Dank! Ihre Anfrage ist bei uns angekommen. Wir melden uns persönlich.'",
     "'Thank you! Your enquiry has reached us. We will get back to you personally.'",
     "'Teşekkürler! Talebiniz bize ulaştı. Size bizzat dönüş yapacağız.'"),
    ("'Senden hat nicht geklappt. Bitte schreiben Sie uns an info@meintex.de.'",
     "'Sending failed. Please email us at info@meintex.de.'",
     "'Gönderim başarısız oldu. Lütfen info@meintex.de adresine yazın.'"),

    # Sprachumschalter: aktive Sprache markieren
    ('<a href="index.html" hreflang="de" class="on">DE</a>\n      <a href="en.html" hreflang="en">EN</a>\n      <a href="tr.html" hreflang="tr">TR</a>',
     '<a href="index.html" hreflang="de">DE</a>\n      <a href="en.html" hreflang="en" class="on">EN</a>\n      <a href="tr.html" hreflang="tr">TR</a>',
     '<a href="index.html" hreflang="de">DE</a>\n      <a href="en.html" hreflang="en">EN</a>\n      <a href="tr.html" hreflang="tr" class="on">TR</a>'),
    # zuletzt, weil kurz: Nav-Button
    ('>Projekt anfragen</a>', '>Request a project</a>', '>Proje talebi</a>'),
]


def build():
    src = (HERE / 'index.html').read_text(encoding='utf-8')
    missing = [de for de, _, _ in T if de not in src]
    for col, name in ((1, 'en.html'), (2, 'tr.html')):
        out = src
        for row in T:
            out = out.replace(row[0], row[col])
        (HERE / name).write_text(out, encoding='utf-8')
        print(f'{name} geschrieben')
    if missing:
        print('\nNICHT GEFUNDEN (Übersetzung prüfen):')
        for m in missing:
            print('  -', m[:90])


if __name__ == '__main__':
    build()
