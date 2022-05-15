# 定义检索文件类

from haystack import indexes
# 导入需要生成检索文件的模型类
from movies.models import moviesInfo

# 索引类的名字 ： 必须固定的  -> 模型的名字 + Index  eg :moviesInfoIndex
class moviesInfoIndex(indexes.SearchIndex,indexes.Indexable):

    # 把索引文件放在同一个文件中
    text = indexes.CharField(document=True,use_template=True)

    # 获取模型数据
    def get_model(self):
        return moviesInfo
    # 建立索引数据
    def index_queryset(self, using=None):
        return self.get_model().objects.all()