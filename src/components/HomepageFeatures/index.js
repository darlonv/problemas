import React from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'Sistemas Operacionais',
    Svg: require('@site/static/img/os.svg').default,
    description: (
      <>
        Teoria, organização e funcionamento de sistemas operacionais.
      </>
    ),
  },
  {
    title: 'Shell',
    Svg: require('@site/static/img/logo.svg').default,
    description: (
      <>
        Comandos, variáveis e utilização.
      </>
    ),
  },
  {
    title: 'Virtualização e Contêineres',
    Svg: require('@site/static/img/algorithm.svg').default,
    description: (
      <>
        Conceitos sobre virtualização, conteinerização e computação em nuvem.
      </>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
