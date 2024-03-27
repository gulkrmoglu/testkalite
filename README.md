PyTest'teki Decoratorler
PyTest, test fonksiyonlarının ve sınıflarının davranışlarını değiştirmek için kullanılabilecek çeşitli decoratorler sunar. En yaygın kullanılan decoratorlerden bazıları şunlardır:

@pytest.fixture: Bu decorator, test fonksiyonları tarafından kullanılabilecek geçici kaynaklar oluşturmak için kullanılır. Fixture'lar, testlerinizin tekrarlanabilir ve bağımsız olmasını sağlar.

@pytest.mark.parametrize: Bu decorator, tek bir test fonksiyonunu birden fazla veri setiyle çalıştırmak için kullanılır. Bu, test kodunuzu daha kısa ve daha okunabilir hale getirebilir.

@pytest.mark.skip: Bu decorator, belirli bir test fonksiyonunun veya sınıfının atlanmasını sağlar.

@pytest.mark.xfail: Bu decorator, belirli bir test fonksiyonunun beklenen şekilde başarısız olmasını sağlar.

@pytest.mark.timeout: Bu decorator, belirli bir test fonksiyonunun belirli bir süre içinde tamamlanmasını sağlar.

@pytest.fixture(autouse=True): Bu decorator, bir fixture'ın test sınıfındaki her test fonksiyonu tarafından otomatik olarak kullanılmasını sağlar.

@pytest.yield_fixture: Bu decorator, bir fixture'ın test fonksiyonu tarafından kullanıldıktan sonra serbest bırakılmasını sağlar.

@pytest.raises: Bu decorator, belirli bir kodun belirli bir hatayı oluşturmasını sağlar.

@pytest.warns: Bu decorator, belirli bir kodun belirli bir uyarıyı oluşturmasını sağlar.

@pytest.deprecated: Bu decorator, belirli bir fonksiyonun veya özelliğin kullanımının eskimiş olduğunu gösterir.
