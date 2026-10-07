import os

file_path = r'd:\TOOLS WEB TOOLS\kiro calorie\src\pages\country\spain\calculadora-de-calorias.astro'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_content = """<section class='p-8 mt-12 mb-8'><h2>Notas Avanzadas de los Practicantes sobre la Salud Metabólica</h2><p>Aunque las fórmulas matemáticas y las pautas generalizadas proporcionadas anteriormente sirven como un excelente punto de partida, la verdadera salud metabólica es altamente individualizada. Las ecuaciones que utilizamos —como la de Mifflin-St Jeor o Harris-Benedict— fueron desarrolladas estudiando promedios poblacionales. Representan una estimación base del gasto energético de tu cuerpo. Sin embargo, tus necesidades diarias reales de energía pueden fluctuar según numerosos factores fisiológicos altamente específicos.</p><p>Por ejemplo, tu Termogénesis por Actividad No Relacionada con el Ejercicio (NEAT) —la energía que quemas a través de movimientos subconscientes como moverte inquietamente, mantener la postura o caminar casualmente— puede variar en cientos de calorías de un día a otro. Una persona que tiene un trabajo muy activo naturalmente tendrá una línea base metabólica significativamente más alta que alguien sedentario, incluso si su edad, peso y altura son idénticos.</p><p>Además, la adaptación metabólica es un fenómeno real. Cuando permaneces en un déficit calórico durante un período prolongado, tu cuerpo intenta intuitivamente conservar energía. Este mecanismo evolutivo de supervivencia significa que a medida que pierdes peso, tu Tasa Metabólica Basal (BMR) disminuye ligeramente, y puedes reducir inconscientemente tu NEAT. Esta es la razón por la que una ingesta calórica que inicialmente causó pérdida de peso puede convertirse eventualmente en tu nuevo nivel de mantenimiento, requiriendo un descanso estratégico de la dieta o un ajuste calórico adicional.</p><p>De manera similar, cuando se está en un superávit calórico (volumen), algunas personas experimentan una regulación al alza en el NEAT. Sus cuerpos queman espontáneamente una parte del exceso de calorías a través del aumento de la producción de calor y el movimiento subconsciente. Esto explica por qué algunas personas tienen dificultades para ganar peso incluso cuando creen que están comiendo un superávit significativo.</p><h3>El Papel de la Densidad de Nutrientes</h3><p>Finalmente, debemos enfatizar que aunque el equilibrio energético (calorías que entran frente a calorías que salen) dicta los cambios en la masa, la distribución de macronutrientes dicta los cambios en la composición corporal, y la densidad de micronutrientes dicta la función fisiológica general. Consumir 2,000 calorías de alimentos ultraprocesados producirá resultados de salud a largo plazo, perfiles hormonales y niveles de energía muy diferentes que consumir 2,000 calorías de alimentos enteros y densos en nutrientes. Recomendamos encarecidamente utilizar estas pautas matemáticas como herramientas dentro de un marco más amplio de nutrición holística y sostenible.</p></section>
</Layout>

<div class="mt-16 bg-canvas-soft dark:bg-gray-800 p-8 rounded-xl">
    <h2 class="text-3xl font-bold mb-6 text-ink dark:text-white">Preguntas Frecuentes y el Impacto Psicológico</h2>
    <p class="text-body dark:text-gray-300 mb-6">Seamos increíblemente honestos por un momento: lidiar con esto puede causar una grave fatiga y ansiedad. No estás solo. Aquí tienes las preguntas más críticas respondidas con total transparencia para proteger tu bienestar mental y asegurarnos de que tengas todos los datos.</p>
    <div class="space-y-6">
        <div>
            <h3 class="text-xl font-semibold text-ink dark:text-white">1. ¿Cómo manejo la ansiedad de tener que hacer esto perfectamente?</h3>
            <p class="text-body dark:text-gray-300 mt-2">La carga psicológica de intentar ser perfecto puede llevar a la parálisis. Los expertos recomiendan centrarse en la regla del 80/20. La consistencia y la precisión general producirán el 90% de los resultados deseados.</p>
        </div>
        <div>
            <h3 class="text-xl font-semibold text-ink dark:text-white">2. ¿Cuáles son los efectos a largo plazo de ignorar estas pautas?</h3>
            <p class="text-body dark:text-gray-300 mt-2">Con el tiempo, la negligencia sistémica se convierte en problemas mayores de salud física y mental. El cumplimiento adecuado mitiga el malestar crónico.</p>
        </div>
        <div>
            <h3 class="text-xl font-semibold text-ink dark:text-white">3. ¿Con qué frecuencia debo reevaluar mis números base?</h3>
            <p class="text-body dark:text-gray-300 mt-2">Se recomienda encarecidamente reevaluar tus medidas y necesidades calóricas cada 3 a 6 meses, o inmediatamente después de cualquier cambio significativo.</p>
        </div>
        <div>
            <h3 class="text-xl font-semibold text-ink dark:text-white">4. ¿Existe algún peligro al depender completamente de calculadoras automatizadas?</h3>
            <p class="text-body dark:text-gray-300 mt-2">Si bien las calculadoras proporcionan un punto de partida matemáticamente sólido, no pueden tener en cuenta la biología humana matizada. Úsalas siempre como guía.</p>
        </div>
    </div>
</div>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{"@type":"Question","name":"¿Cómo manejo la ansiedad de tener que hacer esto perfectamente?","acceptedAnswer":{"@type":"Answer","text":"Los expertos recomiendan centrarse en la regla del 80/20."}}, {"@type":"Question","name":"¿Cuáles son los efectos a largo plazo de ignorar estas pautas?","acceptedAnswer":{"@type":"Answer","text":"La negligencia sistémica se convierte en problemas mayores de salud física y mental."}}]
}
</script>
"""

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines[:115])
    f.write(new_content)
