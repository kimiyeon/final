import { PiAgent } from '@spences10/pi-core'; // Pi SDK 활용 [cite: 62]
import localRecipes from '@/data/recipes.json';

export async function generateRecipe(menuName: string, purpose: string) {
  // 1. 먼저 로컬 recipes.json에 유저가 원하는 메뉴가 있는지 검사 [cite: 132]
  const purposeKey = purpose.toLowerCase();
  const existingMenu = localRecipes[purposeKey]?.find(r => r.menu === menuName);
  
  if (existingMenu) {
    return existingMenu; // 기존 데이터가 있으면 그대로 반환 [cite: 132]
  }

  // 2. [오픈소스 핵심] 로컬에 없는 메뉴라면 AI 에이전트가 실시간 생성 (지식 확장) 
  const recipeAgent = new PiAgent({
    persona: "표준 레시피 및 재료 가이드라인을 정형화하는 맞춤형 영양사" [cite: 58, 322]
  });

  const prompt = `
    사용자가 요청한 메뉴 [${menuName}]의 조리에 필요한 핵심 식재료 목록을 작성해줘.
    반드시 아래의 정형화된 JSON 데이터 포맷만 반환해야 하며, 다른 텍스트는 절대 금지해.
    
    {
      "menu": "${menuName}",
      "ingredients": ["재료키1", "재료키2", "재료키3"]
    }
  `;

  const aiResponse = await recipeAgent.run({ input: prompt });
  return JSON.parse(aiResponse); // 즉석에서 생성된 신규 레시피가 파이프라인에 동적 결합됨! [cite: 164]
}