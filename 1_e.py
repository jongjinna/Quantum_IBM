import qiskit

print(qiskit.__version__)

from qiskit import IBMQ

IBMQ.save_account('8336b11cda16a83758d674d076091ebbeaf397c771a335a694fa2e048f5cda647be15a1c17c06eefad60630f19ab8ecb75150ca72ee029af7f5db79b170082cd')

IBMQ.load_account()

provider = IBMQ.get_provider(group='open')
IBMQ.providers()

print(provider.backends())

# Note : https://ingyeomental.tistory.com/m/15 | https://m.blog.naver.com/PostView.naver?blogId=simhc0714&logNo=221567553302&targetKeyword=&targetRecommendationCode=1
