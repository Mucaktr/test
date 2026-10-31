# Prompt Architect & Executor

Belirsiz bir isteği sınırlı bir plana dönüştürmek, yetki verilen işi yürütmek ve sonucu kontrol etmek için hazırlanmış bir ajan skill'i.

[English](README.md) · [Skill metni](skills/prompt-architect-executor/SKILL.md) · [Paketi indir](skills/prompt-architect-executor.zip)

## Kullanım

Skill metnini okuyun. ZIP'i açın veya `skills/prompt-architect-executor/` klasörünü kullandığınız uygulamanın desteklediği skill konumuna kopyalayın. Ardından o uygulamada gerçekten keşfedildiğini ve çağrılabildiğini doğrulayın; bu yayın uygulama uyumluluğunu kanıtlamaz.

İlk denemeyi küçük ve salt okunur bir işte yapın:

```text
prompt-architect-executor ile bu isteği netleştir ve verdiğim planı incele.
Kısa bir plan kullan; dosya değiştirme, dış servise işlem gönderme.
Hangi kabul ölçütlerinin mevcut malzemeden doğrulanabildiğini açıkla.
```

## Durum

`0.1.0-rc2` bir paketleme ön sürümüdür. Önceki repo adı `test` idi. Skill'in çekirdek yönergeleri korunmuştur. Eski ZIP, Git'teki kaynakla zaten eşleşiyordu; ilk karşılaştırmadaki fark Windows satır sonlarından kaynaklanıyordu. Yeni pakete lisans ve kurulum özeti eklendi. `python -X utf8 scripts/check_package.py` dosya eşliğini kontrol eder.

Paket kontrolü; model davranışını, görev başarısını, uygulamada kurulumu veya production güvenliğini doğrulamaz. Skill yönergeleri uygulamanın üst düzey kurallarının ve izin mekanizmalarının yerine geçmez.

[MIT lisansı](LICENSE) · [Katkı rehberi](CONTRIBUTING.md) · [Güvenlik bildirimi](SECURITY.md)
