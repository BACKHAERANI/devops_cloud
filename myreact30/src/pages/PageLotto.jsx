import Lotto_random_number from "../components/Lotto";

function PageLotto(){
return(
    <>
    <h2>예상 로또번호를 뽑았습니다.</h2>

    <Lotto_random_number color="blue"/>
  

<tr>*위의 번호는 랜덤으로 추첨한 것일 뿐 확률은 예상할 수 없습니다.</tr>
</>
)
};

export default PageLotto;